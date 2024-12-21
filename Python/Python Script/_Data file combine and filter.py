# libraries required
# pip install Openpyxl
# pip install pandas
# pip install xlrd


#for converting general
def excel_date_to_datetime(excel_date):
    import pandas as pd
    from datetime import datetime, timedelta
    return datetime(1899, 12, 30) + timedelta(days=excel_date)

  
def get_Data_file(file_name_to_be_created, initial_date, final_date):
    
    print("")
    print(r"Running script '_Data_file_combine_and_filter' now")
    
    # below code should combine data from multiple excel workbook having multiple sheets and filter by date into new workbook
    #we have 3 workbook Data.xlsb --empty, Tran.xlsb, Binextgen.xlsb
    import pandas as pd
    
    file_path_data_file = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Daily_data\\Data.xlsb' #xlsx excel workbook .xlsb  excel binary
    
    df_data_file = pd.ExcelFile(file_path_data_file) # Creating an ExcelFile object 
    
    sheet_names_data_file = df_data_file.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']
    
    dict_data_file = {} # to get data sheetwise in dictionary sheet wise in key - value pair
    
    for sheet in sheet_names_data_file:
        dict_data_file[sheet] = pd.read_excel(df_data_file,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)
    
    # DID = pd.read_excel(file1, sheet_name=0, header=None, usecols=[0, 1, 6], names=['A', 'ID', 'B'], dtype={2:str}, skiprows=10)
    
    # For example...
    # usecols => read only specific col indexes
    # dtype => specifying the data types
    # skiprows => skip number of rows from the top.
    
    print("")
    print("Got Data file")
    # print(dict_data_file)
    
    #################################################################################################################
    
    file_path_tran_file = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\Daily_data\\Tran.xlsb' #xlsx excel workbook .xlsb  excel binary
    
    df_tran_file = pd.ExcelFile(file_path_tran_file) # Creating an ExcelFile object 
    
    sheet_names_tran_file = df_tran_file.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']
    
    dict_tran_file = {} # to get data sheetwise in dictionary sheet wise in key - value pair
    
    for sheet in sheet_names_tran_file:
        dict_tran_file[sheet] = pd.read_excel(df_tran_file,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)
        # Assuming 'df' is your DataFrame and 'date_column' is the column with Excel date numbers
        # df['date_column'] = pd.to_datetime(df['date_column'].apply(excel_date_to_datetime))
        dict_tran_file[sheet]["Date"] = pd.to_datetime(dict_tran_file[sheet]["Date"].apply(excel_date_to_datetime)) # converting excel general date into date
        # df['INSERT_DATE_'] = pd.to_datetime(df['INSERT_DATE'],format='%Y-%m-%d')
        # dict_tran_file[sheet]["Date"] = pd.to_datetime(dict_tran_file[sheet]["Date"],format='%Y-%m-%d') # converting datetime to date

    print("")
    print("Got Tran file data")
    # print(dict_tran_file)
    
    #################################################################################################################
    
    file_path_binextgen_file = 'C:\\Users\\IN10033204\\OneDrive - R1\\Documents\\\\Daily_data\\Binextgen.xlsb' #xlsx excel workbook .xlsb  excel binary
    
    df_binextgen_file = pd.ExcelFile(file_path_binextgen_file) # Creating an ExcelFile object 
    
    sheet_names_binextgen_file = df_binextgen_file.sheet_names #Print the sheet names ['Payment', 'AR_', 'Charges', 'Released', 'Activity', 'Remits', 'Adjustment']
    
    dict_binextgen_file = {} # to get data sheetwise in dictionary sheet wise in key - value pair
    
    for sheet in sheet_names_binextgen_file:
        dict_binextgen_file[sheet] = pd.read_excel(df_binextgen_file,sheet,header=None ,usecols=[0, 1,2,3,4], names = ['Source','Facility','Accounts','Amount','Date'] ,skiprows = 1) # Load an Excel file into a DataFrame (read_excel)
        dict_binextgen_file[sheet]["Date"] = pd.to_datetime(dict_binextgen_file[sheet]["Date"].apply(excel_date_to_datetime)) # converting excel general date into date
        # dict_binextgen_file[sheet]["Date"] = pd.to_datetime(dict_binextgen_file[sheet]["Date"],format='%Y-%m-%d') # converting datetime to date

    print("")
    print("Got BiNextGen file data")
    # print(dict_binextgen_file)
    
    #################################################################################################################
    
    # Append new data
    # df_combined = df_existing.append(df_new, ignore_index=True)
    
    dict_combined = {} # to combine data from 2 sheets
    
    for sheet in sheet_names_data_file:
        dict_combined[sheet] = pd.concat([dict_data_file[sheet] , dict_tran_file[sheet] ,dict_binextgen_file[sheet] ], ignore_index=True, axis=0) #axis = 0 for row wise concat
    
    print("")
    print("Data compliation completed")
    # print(dict_combined)
    
    ##################################################################################################################
    
    #change filter dates according to general formatting in excel
    
    
    
    for sheet in sheet_names_data_file:
        dict_combined[sheet] = dict_combined[sheet].loc[(dict_combined[sheet]['Date'] >= initial_date) & (dict_combined[sheet]['Date'] <= final_date)] #filtering
        dict_combined[sheet]['Date']= pd.to_datetime(dict_combined[sheet]['Date']).dt.date  #convert datetime into date
        # dict_combined[sheet] is df here
        # df_filter = dict_combined[sheet].query('Date > @initial_date and Date < @final_date')

    print("")
    print("got combined data filtered sheet wise")
    # print(dict_combined)
        
    with pd.ExcelWriter(file_name_to_be_created,engine="openpyxl") as writer: #creating ExcelWriter object
        for sheet in sheet_names_data_file:
            dict_combined[sheet].to_excel(writer, sheet_name=sheet, index=False)

    print("")
    print('Done! '+file_name_to_be_created+' is created in current directory')
    print("Good Bye")

    
########################################################################

file_name_to_be_created = input("Enter file name to be for Data file: ")

initial_date = input(r"Enter initial date for Data file in 'YYYY-MM-DD' format : ")

final_date = input(r"Enter final date for Data file in 'YYYY-MM-DD' format : ")

if not (file_name_to_be_created.endswith(".xlsx" or ".xlsb")):
    file_name_to_be_created +=".xlsx" #for binary .xlsb
    get_Data_file(file_name_to_be_created, initial_date, final_date) # calling function
    
else:
    print("enter without .xlsx or .xlsb for excel files")
