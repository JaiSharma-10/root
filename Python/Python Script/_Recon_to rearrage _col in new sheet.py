# libraries required
# pip install Openpyxl
# pip install pandas
# pip install xlrd

# Below code should combine pick and choose coulmn from excel file multiple sheets and filter by date into new workbook
# we have 1 workbook Recon.xlsb 

import pandas as pd


file_path = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Daily_data\\Recon.xlsx' #recon file

df = pd.ExcelFile(file_path) # Creating an ExcelFile object 

sheet_names = df.sheet_names # function giving the sheet names

list_of_sheet = ['AR_Total','AR_Valid','Charges_Total','Charges_Valid','Payment_Total','Payment_Valid','Adjustment_Total','Adjustment_Valid']

df_AR_Total = pd.read_excel(df,sheet_name = 'Ar',header=None ,usecols=[0,2,3,7,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_AR_Valid = pd.read_excel(df,sheet_name = 'Ar',header=None ,usecols=[1,2,3,11,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Charges_Total = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[0,2,3,4,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Charges_Valid = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[1,2,3,7,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Payment_Total = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[0,2,3,5,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Payment_Valid = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[1,2,3,9,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Adjustment_Total = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[0,2,3,6,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

df_Adjustment_Valid = pd.read_excel(df,sheet_name = 'Other',header=None ,usecols=[1,2,3,10,12] , names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

file_name_to_be_created = "Output_Recon_1220.xlsx"

with pd.ExcelWriter(file_name_to_be_created ,engine="openpyxl") as writer:
    df_AR_Total.to_excel(writer, sheet_name='AR_Total', index=False)
    df_AR_Valid.to_excel(writer, sheet_name='AR_Valid', index=False)
    df_Charges_Total.to_excel(writer, sheet_name='Charges_Total', index=False)
    df_Charges_Valid.to_excel(writer, sheet_name='Charges_Valid', index=False)
    df_Payment_Total.to_excel(writer, sheet_name='Payment_Total', index=False)
    df_Payment_Valid.to_excel(writer, sheet_name='Payment_Valid', index=False)
    df_Adjustment_Total.to_excel(writer, sheet_name='Adjustment_Total', index=False)
    df_Adjustment_Valid.to_excel(writer, sheet_name='Adjustment_Valid', index=False)

# print(df_AR_Total)
# print(df_AR_Valid)
# print(df_Charges_Total)
# print(df_Charges_Valid)
# print(df_Payment_Total)
# print(df_Payment_Valid)
# print(df_Adjustment_Total)
# print(df_Adjustment_Valid)


print("")

print('Done! '+file_name_to_be_created+' is created in current directory')

print("Good Bye")
