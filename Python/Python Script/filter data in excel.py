# below code can filter excel file by column value

import pandas as pd

# Path to the local Excel file
file_path = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Data_1206.xlsx' #xlsx excel workbook .xlsb  excel binary


df = pd.ExcelFile(file_path) # Creating an ExcelFile object 

# Get the sheet names using The sheet_names property that will generate a list of the sheet names in the file.
sheet_names = df.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']

# creating dictionary to list of each sheets and dataframe object
# pd.read_excel is used to read the excel file data into a DataFrame object
dict = {}

for sheet in sheet_names:
    # Load an Excel file into a DataFrame read_excel
    dict[sheet] = pd.read_excel(df,sheet,header = 0 ) #header: The row number to use as the header (0-indexed, defaults to 0).
# above code will hold sheet name as keys and whole data as its value

# for example Payment : dict['Payment'] is the data frame where Payment is key and dict['Payments'] is dataframe #print(dict['Payment'])

df_whole_data = pd.DataFrame()

df_filter_sheet = pd.DataFrame() #creating empty dataframe

print(df_filter_sheet)

start_date = 45565
end_date = 45630


with pd.ExcelWriter("output_Data_1206_2.xlsx" ,engine="openpyxl") as writer:
    for sheet in sheet_names:
        df_filter = dict[sheet].query('Date > @start_date and Date < @end_date')
        df_filter.to_excel(writer, sheet_name=sheet, index=False)


# To write to multiple sheets it is necessary to create an ExcelWriter object with a target file name, and specify a sheet in the file
# to write to. Multiple sheets may be written to by specifying unique sheet_name . With all data written to the file it is necessary to 
# save the changes
