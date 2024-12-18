#this script can get data from MS SQL with no username and password

import pyodbc #This library is used to connect to databases using ODBC.
#from sqlalchemy import create_engine
import pandas as pd #data manipulation and analysis.


try:
    
    list = ['ALPSTAGE13.accretivehealth.local','ALPSTAGE14.accretivehealth.local','ALPSTAGE15.accretivehealth.local','AHV-A2ASTG18.EXTAPP.LOCAL']
    #,'AHS-STAGE02.accretivehealth.local','AHS-STAGE03.accretivehealth.local','AHS-STAGE04.accretivehealth.local','AHS-Stage05.accretivehealth.local','ALPSTAGE09.accretivehealth.local','ALPSTAGE10.accretivehealth.local','ALPSTAGE12.accretivehealth.local']

    df_combined = pd.DataFrame()
    
    for element in list:
        
        cnxn = pyodbc.connect(
                r'Driver={SQL Server};'
                r'Server='+element+',1433;'  # element will have server name
                #r'Database=;'
                r'Trusted_Connection=yes;' # Trusted_Connection=yes, which typically means it uses the Windows credentials of the user running the script.
            )
    
        print("server->"+element)

        cursor = cnxn.cursor()
            
        print("Connection established.")
        
        query = """
            SET NOCOUNT ON
            IF
                object_id('tempdb..#temp') IS NOT NULL
                DROP TABLE #temp
                SET
                        QUOTED_IDENTIFIER ON
                CREATE TABLE #temp
                        (
                                Facilitycode         VARCHAR(5) NULL  ,
                                PatientAccountNbr    VARCHAR(50) NULL ,
                                EncounterOpenBalance MONEY            ,
                                fileDate             DATE
                        )
                EXEC sp_MSforeachdb 'IF left(''?'',5) =''Stage''
            BEGIN
            use ?
            Set QUOTED_IDENTIFIER On
            insert into #temp
            Select right (db_name(),4)Facilitycode,Count(PatientAccountNbr) accounts,SUM(TRY_CAST(EncounterOpenBalance as money))
            OpenBalance,cast (fileDate as date) Date from RETRO07D (nolock)
            Where
            TRY_CAST(EncounterOpenBalance as money) IS NOT NULL
            AND
            TRY_CAST(EncounterOpenBalance as money) > 0
            and FacilityCode <>''TRAILER''
            and fileDate > ''2024-10-01''
            and AccountStatus <>''OFC''
            group by fileDate order by 1 desc
            end'
                SELECT
                        *
                FROM
                        #temp"""
            
        df = pd.read_sql(query, cnxn) #get data from sql to dataframe

        df_combined = pd.concat([df,df_combined],ignore_index=True, axis=0) #it combines data from various servers in list

    print(df_combined)

    df_combined.to_excel('Test_Tran_AR_04.xlsx', sheet_name='sheet', index=False)
    

except pyodbc.Error as e:
    print("Error in connection:", e)
    
finally:
    if 'cnxn' in locals() and cnxn:
        cnxn.close()