import pandas as pd
import snowflake.connector

credentials = {
    'account'    : 'mt59224.east-us-2.privatelink'
    , 'user'     : 'JSHARMA10@R1RCM.COM'
    , 'authenticator' : 'externalbrowser'
    ,'warehouse' : 'BISON_BI_WH_M',
    'database' : 'RCM',
    'schema' : 'RCM_DATAMART',
    'authanticator' :'externalbrowser'
    }
 
    with snowflake.connector.connect(**credentials) as cnx:  #**kwargs in function definitions in Python is used to pass a keyworded
    cur  = cnx.cursor()
    cur.execute('''             
        select distinct
                *
        from
                (
                        SELECT
                                YEAR(DATEADD(MONTH, +6, txn_date)) AS FiscalYear,
                                sum(txn_amt)                       as TXNAMOUNT ,
                                facility_group_name                             ,
                                b.facility_group_name                           ,
                                txn_code_subcategory
                        FROM
                                RCM_DATAMART.fact_transaction a
                        left join
                                RCM_DATAMART.dim_facility b
                        on
                                a.facility_code = b.facility_code
                        where
                                txn_code_category in ('Denial - clinical',
                                                    'denial - technical')
                        and     b.facility_group_name = 'Baltimore'
                        group by
                                facility_group_name ,
                                FiscalYear          ,
                                txn_code_subcategory,
                                b.facility_group_name)
        where
                fiscalyear = 2024''')
    

text = cur.fetchall() # list of tuple

text_for_example = [(1,2,3,4,5),(6,7,8,9,10)]

list_of_col = ['FiscalYear','TXNAMOUNT', 'facility_group_name', 'b.facility_group_name', 'txn_code_subcategory'] 

df = pd.DataFrame(columns = list_of_col )
    
for element  in text_for_example:
    individual_row_data = [data for data in element] 
    # list comprehension
    # [1, 2, 3, 4, 5]
    # [6, 7, 8, 9, 10]
    length = len(df) # assign row count of df
    df.loc[length]  = individual_row_data
    
print(df)
    
 # here account -> mt59224.east-us-2.privatelink if checked by link of SNOWFLAKE between https:// and .snowflakecomputing
 ######################################################################