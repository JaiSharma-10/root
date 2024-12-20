# libraries required
# pip install Openpyxl
# pip install pandas
# pip install xlrd

file_name_to_be_created = input("Enter file name to be for recon file: ")

initial_date = input(r"Enter initial_date for recon file in 'YYYY-MM-DD' format : ")

final_date = input(r"Enter initial_date for recon file in 'YYYY-MM-DD' format : ")

if not (file_name_to_be_created.endswith(".xlsx" or ".xlsb")):

    file_name_to_be_created +=".xlsx" #for binary .xlsb
    
    def get_Recon(file_name_to_be_created):
        
        print(r"Running script '_Recon_File_arrange_filter_sql' now")

        #time taken 2:39
        #get recon data 
        
        import pandas as pd  #data manipulation and analysis.#
        import pyodbc #This library is used to connect to databases using ODBC.
        
        #creating connection string
        cnxn = pyodbc.connect(
            r'Driver={SQL Server};'
            r'Server=AHV-SISDRCSTG01.accretivehealth.local;'
            #r'Database='
            r'Trusted_Connection=yes;' # Trusted_Connection=yes, which typically means it uses the Windows credentials of the user running the script.
        )
        
        cursor = cnxn.cursor() #creating cursor object for cnxn
        
        print("Connection established.")
        
        query = """
                        
        SET ANSI_WARNINGS OFF
        ----performance tuning concepts of SQL Server
        SET NOCOUNT ON
        
        DECLARE @DatabaseName NVARCHAR(128)
        DECLARE @SQL NVARCHAR(MAX) = ''
        
        DECLARE DatabaseCursor CURSOR FOR
        --there are more databases in Tran than you'll find data in R1BI for.  So I'm limiting the databases to what is loaded into R1BI
        SELECT name
        FROM sys.databases
        WHERE state = 0 -- Online databases only
        and right(name,3) = 'DRC'
        order by name
        
        
        
        OPEN DatabaseCursor
        FETCH NEXT FROM DatabaseCursor INTO @DatabaseName
        
        WHILE @@FETCH_STATUS = 0
        BEGIN
            -- Step 2: Build the union query
            SET @SQL = @SQL + 'SELECT a.FAC_CODE, A.post_DATE, A.INSERT_DATE, A.TOT_CHRGS, A.TOT_PYMTS *-1 TOT_PYMTS,A.Tot_Adj *-1 Tot_Adj, A.TOT_AR, A.VALID_TOTAL_CHRGS, A.VALID_TOTAL_PMNTS *-1 VALID_TOTAL_PMNTS,A.VALID_TOTAL_Adj *-1 VALID_TOTAL_Adj, A.VALID_TOTAL_AR
                                FROM ' + QUOTENAME(@DatabaseName) + '.dbo.DATA_RECON a with (nolock)
                                UNION ALL '
        
        
                            
            FETCH NEXT FROM DatabaseCursor INTO @DatabaseName
        END
        
        CLOSE DatabaseCursor
        DEALLOCATE DatabaseCursor
        
        -- Remove the last 'UNION ALL' from the query
        SET @SQL = LEFT(@SQL, LEN(@SQL) - LEN('UNION ALL '))
        
        -- Step 3: Execute the union query
        EXEC sp_executesql @SQL
        
        
        SET NOCOUNT OFF
        
        """
                            
        df = pd.read_sql(query, cnxn) #get data from sql to dataframe
        
        df['source_1'] = 'Recon_Total'
        
        df['source_2'] = 'Recon_Total'
        
        df['X'] = ''
        
        # Convert the datetime column to a date column and filtering it out
        
        df['INSERT_DATE_'] = pd.to_datetime(df['INSERT_DATE'],format='%Y-%m-%d')
        
        df['post_DATE_'] = pd.to_datetime(df['post_DATE'],format="%Y-%m-%d")
        
        filtered_df_insert_date = df.loc[(df['INSERT_DATE_'] >= initial_date) & (df['INSERT_DATE_'] <= final_date)] #filtering
        
        filtered_df_insert_date['INSERT_DATE_0']= pd.to_datetime(df['INSERT_DATE_']).dt.date  #convert datetime into date
        
        filtered_df_post_date = df.loc[(df['post_DATE_'] >= initial_date) & (df['post_DATE_'] < final_date)] #filtering
        
        filtered_df_post_date['post_DATE_0']= pd.to_datetime(df['post_DATE_']).dt.date  #convert datetime into date
        
        
        column_names = list(df.columns)
        
        print("got data")
        
        print(column_names)
        #df.to_excel('Recon_1.xlsx', sheet_name='sheet', index=False)
        
        #['FAC_CODE', 'post_DATE', 'INSERT_DATE', 'TOT_CHRGS', 'TOT_PYMTS', 'Tot_Adj', 'TOT_AR', 'VALID_TOTAL_CHRGS', 'VALID_TOTAL_PMNTS',
        #  'VALID_TOTAL_Adj', 'VALID_TOTAL_AR', 'source_1', 'source_2']
        
        
        #dateframe source wise
        df_AR_Total = filtered_df_insert_date[['source_1','FAC_CODE','X','TOT_AR','INSERT_DATE_0']]  #insert
        
        df_Charges_Total = filtered_df_post_date[['source_1','FAC_CODE','X','TOT_CHRGS','post_DATE_0']]
        
        df_Payment_Total = filtered_df_post_date[['source_1','FAC_CODE','X','TOT_PYMTS','post_DATE_0']]
        
        df_Adjustment_Total = filtered_df_post_date[['source_1','FAC_CODE','X','Tot_Adj','post_DATE_0']]
        
        df_AR_Valid = filtered_df_insert_date[['source_2','FAC_CODE','X','VALID_TOTAL_AR','INSERT_DATE_0']] #insert
        
        df_Charges_Valid = filtered_df_post_date[['source_2','FAC_CODE','X','VALID_TOTAL_CHRGS','post_DATE_0']] 
        
        df_Payment_Valid = filtered_df_post_date[['source_2','FAC_CODE','X','VALID_TOTAL_PMNTS','post_DATE_0']] 
        
        df_Adjustment_Valid = filtered_df_post_date[['source_2','FAC_CODE','X','VALID_TOTAL_Adj','post_DATE_0']] 
        
        
        with pd.ExcelWriter(file_name_to_be_created ,engine="openpyxl") as writer:
            df_AR_Total.to_excel(writer, sheet_name='AR_Total', index=False)
            df_AR_Valid.to_excel(writer, sheet_name='AR_Valid', index=False)
            df_Charges_Total.to_excel(writer, sheet_name='Charges_Total', index=False)
            df_Charges_Valid.to_excel(writer, sheet_name='Charges_Valid', index=False)
            df_Payment_Total.to_excel(writer, sheet_name='Payment_Total', index=False)
            df_Payment_Valid.to_excel(writer, sheet_name='Payment_Valid', index=False)
            df_Adjustment_Total.to_excel(writer, sheet_name='Adjustment_Total', index=False)
            df_Adjustment_Valid.to_excel(writer, sheet_name='Adjustment_Valid', index=False)
        
        
        print(df_AR_Total)
        print(df_Charges_Total)
        
        #print(df_Charges_Total)
        
    get_Recon(file_name_to_be_created) # calling function
    
else:
    print("enter without .xlsx or .xlsb for excel files")
