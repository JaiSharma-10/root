#this script can get data from MS SQL with no username and password

import pyodbc
from sqlalchemy import create_engine
import pandas as pd


try:
    cnxn = pyodbc.connect(
        r'Driver={SQL Server};'
        r'Server=AHS-Care05.accretivehealth.local,1433;'  # Assuming the default port 1433
        r'Database=master;'
        r'Trusted_Connection=yes;'
    )
    cursor = cnxn.cursor()
    print("Connection established.")

    query = r"Select Encounterid,Amount*-1 amnt,Cast (postdate as Date) Postdate from TranAAIL.dbo.Payments (nolock) ;"
    
    df = pd.read_sql(query, cnxn)

    print(df.head(26))

except pyodbc.Error as e:
    print("Error in connection:", e)
finally:
    if 'cnxn' in locals() and cnxn:
        cnxn.close()