# Below code should combine data from multiple excel workbook having multiple sheets and filter by date into new workbook
# we have Tran and BING file it will combine and filter by date 
# script can be extend for multiple source
# we have 3 workbook Data.xlsb --empty, Tran.xlsb, Binextgen.xlsb
import pandas as pd

# libraries
# pip install Openpyxl
# pip install pandas

file_path_1 = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Daily_data\\Data.xlsb' #xlsx excel workbook .xlsb  excel binary

df_1 = pd.ExcelFile(file_path_1) # Creating an ExcelFile object 

sheet_names_1 = df_1.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']

dict_1 = {} # to get data sheetwise in dictionary sheet wise in key - value pair

for sheet in sheet_names_1:
    dict_1[sheet] = pd.read_excel(df_1,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

# DID = pd.read_excel(file1, sheet_name=0, header=None, usecols=[0, 1, 6], names=['A', 'ID', 'B'], dtype={2:str}, skiprows=10)

# For example...
# usecols => read only specific col indexes
# dtype => specifying the data types
# skiprows => skip number of rows from the top.

# print("File 1 data")
# print(dict_1)

#################################################################################################################

file_path_2 = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Daily_data\\Tran.xlsb' #xlsx excel workbook .xlsb  excel binary

df_2 = pd.ExcelFile(file_path_2) # Creating an ExcelFile object 

sheet_names_2 = df_2.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']

dict_2 = {} # to get data sheetwise in dictionary sheet wise in key - value pair

for sheet in sheet_names_2:
    dict_2[sheet] = pd.read_excel(df_2,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

# print("File 2 data")
# print(dict_2)

#################################################################################################################

file_path_3 = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\\\Daily_data\\Binextgen.xlsb' #xlsx excel workbook .xlsb  excel binary

df_3 = pd.ExcelFile(file_path_3) # Creating an ExcelFile object 

sheet_names_3 = df_3.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']

dict_3 = {} # to get data sheetwise in dictionary sheet wise in key - value pair

for sheet in sheet_names_3:
    dict_3[sheet] = pd.read_excel(df_3,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)

# print("File 3 data")
# print(dict_3)
################################################################################################################

# Append new data
# df_combined = df_existing.append(df_new, ignore_index=True)

dict_combined = {} # to combine data from 2 sheets

for sheet in sheet_names_1:
    dict_combined[sheet] = pd.concat([dict_1[sheet] , dict_2[sheet] ,dict_3[sheet] ], ignore_index=True, axis=0) #axis = 0 for row wise concat

#print("File combination")
#print(dict_combined)

##################################################################################################################

#change filter dates according to general formatting in excel

start_date = 45565
end_date = 45641

file_name_to_be_created = "Output_Data_1217_1.xlsx" 

with pd.ExcelWriter(file_name_to_be_created,engine="openpyxl") as writer: #creating ExcelWriter object
    for sheet in sheet_names_1:
        df_filter = dict_combined[sheet].query('Date > @start_date and Date < @end_date')
        df_filter.to_excel(writer, sheet_name=sheet, index=False)

print('Done! '+file_name_to_be_created+' is created in current directory')
