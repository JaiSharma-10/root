#this script can get data from MS SQL with no username and password

# Note there is errror in two server apart from that this script is working fine

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
    list = ['ALPSTAGE13.accretivehealth.local','ALPSTAGE14.accretivehealth.local','ALPSTAGE15.accretivehealth.local','AHV-A2ASTG18.EXTAPP.LOCAL','AHS-STAGE02.accretivehealth.local','AHS-STAGE03.accretivehealth.local','AHS-Stage05.accretivehealth.local','ALPSTAGE09.accretivehealth.local','ALPSTAGE10.accretivehealth.local','ALPSTAGE12.accretivehealth.local']

    #'AHS-STAGE04.accretivehealth.local', #error
    
    

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

       # df = pd.read_sql(query, cnxn) 
       # Issue-> read_sql in pandas doesn't directly iterate through null values
       # TypeError: 'NoneType' object is not iterable

        print("Got data for "+element+" from sql to dataframe")
        
        print(len(df))

        df_Recon07 = pd.concat([df,df_Recon07],ignore_index=True, axis=0) #it combines data from various servers in list

    #Recon06
    ######################################################################
   
    #'ALPSTAGE11.accretivehealth.local'
    #error

    list = ['ALPSTAGE10.accretivehealth.local','ALPSTAGE12.accretivehealth.local','ALPSTAGE13.accretivehealth.local']
    
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
            OpenBalance,cast (fileDate as date) Date from RETRO06D (nolock)
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

        print("Got data for "+element+" from sql to dataframe")
        
        # df = pd.read_sql(query, cnxn) 
        # Issue-> read_sql in pandas doesn't directly iterate through null values
        # TypeError: 'NoneType' object is not iterable


        df_Recon06 = pd.concat([df,df_Recon06],ignore_index=True, axis=0) #it combines data from various servers in list


    #Recon04
    ######################################################################
   
    list = ['ALPSTAGE08.accretivehealth.local']
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
            OpenBalance,cast (fileDate as date) Date from RETRO04D (nolock)
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

        print("Got data for "+element+" from sql to dataframe")

        df_Recon04 = pd.concat([df_Recon07,df_Recon06,df_Recon04],ignore_index=True, axis=0) #it combines data from various servers in list
        
    #####################################################################################################################
    
    df_combined = pd.concat([df,df_Recon04],ignore_index=True, axis=0)

    file_name_to_be_created = 'Tran_AR_Data_1218.xlsx'

    df_combined.to_excel(file_name_to_be_created, sheet_name='sheet', index=False)

    print('All Done! '+file_name_to_be_created+' is created in current directory')

    print("Good Bye")
    

except pyodbc.Error as e:
    print("Error in connection:", e)
    
finally:
    if 'cnxn' in locals() and cnxn:
        cnxn.close()