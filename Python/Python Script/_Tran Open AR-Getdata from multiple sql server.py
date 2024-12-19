#this script can get data from MS SQL with no username and password

# note this the errro in two server this script is working fine

#AHS-STAGE04
#ALPSTAGE11

import pyodbc #This library is used to connect to databases using ODBC.
#from sqlalchemy import create_engine
import pandas as pd #data manipulation and analysis.


try:
    
    df_combined = pd.DataFrame() #df to hold combined data
    df_Recon07 = pd.DataFrame()
    df_Recon06 = pd.DataFrame()
    df_Recon04 = pd.DataFrame()
    
    #Recon07
    ######################################################################
    #'AHS-STAGE04.accretivehealth.local'
    list = ['AHS-STAGE04.accretivehealth.local','ALPSTAGE11.accretivehealth.local']

    for element in list:
        
        cnxn = pyodbc.connect(
                r'Driver={SQL Server};'
                r'Server='+element+',1433;'  # element will have server name
                #r'Database=;'
                r'Trusted_Connection=yes;' # Trusted_Connection=yes, which typically means it uses the Windows credentials of the user running the script.
            )
    
        print("server-> "+element)

        cursor = cnxn.cursor()
            
        print("Connection established.")
        
        query = """
            SET ANSI_WARNINGS OFF
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

        print(len(df))

       # df = pd.read_sql(query, cnxn) 
       # Issue-> read_sql in pandas doesn't directly iterate through null values
       # TypeError: 'NoneType' object is not iterable

       # got solution

       #ignoring/disregarding warning messages in SSMS, which, I believe, results in cursor not being a query and pyodbc throwing ProgrammingError "No results. Previous SQL was not a query."
        # The warning:
        # Warning: Null value is eliminated by an aggregate or other SET operation.
        # SET ANSI_WARNINGS OFF solved the issue.
        # Inserting "SET ANSI_WARNINGS OFF" at the beginning of SQL query worked.



        print("Got data for "+element+" from sql to dataframe")
    
        df_combined = pd.concat([df,df_combined],ignore_index=True, axis=0)


    df_combined.to_excel('Test_Tran_AR_01.xlsx', sheet_name='sheet', index=False)
    

except pyodbc.Error as e:
    print("Error in connection:", e)
    
finally:
    if 'cnxn' in locals() and cnxn:
        cnxn.close()
