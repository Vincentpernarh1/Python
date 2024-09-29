import os
import pandas as pd

# Define relevant rows, normalized to lower case for consistency
relevant_rows = [
    "automóvel novo",
    "emplacamento e licença",
    "seguro voluntário de veículo",
    "multa",
    "óleo lubrificante",
    "acessórios e peças",
    "pneu",
    "conserto de automóvel",
    "estacionamento",
    "pedágio",
    "lubrificação e lavagem",
    "automóvel usado",
    "pintura de veículo",
    "aluguel de veículo",
    "motocicleta"
]

columns = [
    "Item",  # This will hold the row names
    "RJ", "POA", "BH", "REC", "SP", "DF", "BEL", "FOR", "SAL", "CUR", "GOI",
    "VIT", "CG", "RB", "SL", "AJU", "NACIONAL", "Date"
]

# Set the directory where your datasets are stored
data_directory = 'C:/Users/sd74216/Desktop/Vpena/Python_excel_Automation/INPC/datas_below_2011'
master_file_path = os.path.join(data_directory, 'master_filtered_data.xlsx')

# List all files in the data directory
files = [f for f in os.listdir(data_directory) if f.endswith('.xls') or f.endswith('.xlsx')]

# Initialize an empty DataFrame to accumulate filtered data
master_df = pd.DataFrame(columns=columns)

for file_name in files:
    # Construct the full file path
    file_path = os.path.join(data_directory, file_name)
    
    # Determine the engine based on the file extension
    if file_name.endswith('.xlsx'):
        engine = 'openpyxl'
    else:
        engine = 'xlrd'  # For .xls files
    
    try:
        # Load the Excel file with the appropriate engine
        xls = pd.ExcelFile(file_path, engine=engine)
        
        # Print sheet names to understand the structure
        print(f"Processing '{file_name}'...")
    
    except Exception as e:
        print(f"Failed to process '{file_name}' due to: {e}")
        continue  # Skip to the next file
    
    sheet_name = xls.sheet_names[0]
    print(sheet_name)

    # Extract date code from the filename
    parts = file_name.split('_')
    date_code = parts[1][:6]  # Extract '202402' part from '202402Subitem.xls'

    # Read the data from the sheet with the appropriate header
    #f date_code > "201101" and date_code < "20112" :
    header_row = 4
    
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)
    

    # Initialize an empty list to store the extracted names
    name = []
    found = 0
#     if date_code <"201107" :
#         size = int(len(df))-1
#     else:
#         size = int(len(df))

#     # Iterate through the rows in the DataFrame
#     for i in range(0, size):
#         # Check if the value in the 2nd column (index 2) contains a hyphen
#         found = 1
#         if  '-' in str(df.iloc[i, 0]):
#             # Split the string by the hyphen and take the second part
#             split_name = df.iloc[i, 0].split('-')
#             if len(split_name) > 1:
#                 name.append(split_name[1].strip().lower())
#             else:
#                 name.append(df.iloc[i, 0].strip().lower())
        
#         elif  isinstance(df.iloc[i, 1], str) :
#                 found = 1
#                 if '-' in str(df.iloc[i, 1]) :
#                     # Split the string by the hyphen and take the second part
#                     split_name = df.iloc[i, 1].split('-')
#                     if len(split_name) > 1:
#                         name.append(split_name[1].strip().lower())
#                     else:
#                         name.append(df.iloc[i, 1].strip().lower())
#         elif  isinstance(df.iloc[i, 2], str) :
#             found = 1
#             if '-' in df.iloc[i, 2] :
#                 # Split the string by the hyphen and take the second part
#                 split_name = df.iloc[i, 2].split('-')
#                 if len(split_name) > 1:
#                     name.append(split_name[1].strip().lower())
#                 else:
#                     name.append(df.iloc[i, 2].strip().lower())
#         elif  isinstance(df.iloc[i, 0], str) :
#             found = 0
#             # If there is no hyphen, just take the value as is, converting to lowercase and stripping whitespace
#             #name.append(str(df.iloc[i, 0]).strip().lower())
        
        
#         #print(name)

#         # Print the first 5 elements to verify the extraction process
    
#         # Assign the extracted names to the first column of the DataFrame
#     if found ==1 :
#         df.iloc[:, 0] = name
#         # Assuming df is your DataFrame
#         df_filtered_row = df[df.iloc[:, 0].isin(relevant_rows)].copy()

#         # Remove columns 1 to 3 (0-indexed, so these are columns 0, 1, 2)
#         df_filtered_row = df_filtered_row.drop(df_filtered_row.columns[1:3], axis=1)
#     else :
#         df.iloc[:, 0] = df.iloc[:, 0] 
#         df_filtered_row = df[df.iloc[:, 0].isin(relevant_rows)].copy()

#     #print(df.iloc[0:, 0])

#     print(df)

   

#     #print(df_filtered_row)
    
    # Ensure the first column is a string, trim whitespace, and convert to lowercase
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip().str.lower()
    
    # Filter rows based on relevant_rows
    df_filtered_row = df[df.iloc[:, 0].isin(relevant_rows)].copy()
    
    # Rename the first column to 'Item' to include it in the final DataFrame
    df_filtered_row.rename(columns={df.columns[0]: "Item"}, inplace=True)
    
#     # Reindex columns according to the predefined list and fill missing columns with "-"
    df_filtered_row = df_filtered_row.reindex(columns=columns,fill_value="-")
    
    # exit()
    
    # Add the extracted date code to the 'Date' column
    df_filtered_row['Date'] = date_code
    
    # Append filtered data to the master DataFrame
    master_df = pd.concat([master_df, df_filtered_row], ignore_index=True)
    
    # Save the master DataFrame to a new file
    master_df.to_excel(master_file_path, index=False, engine='openpyxl')
    print(df_filtered_row)
    #exit()
print(f"All filtered data has been saved to '{master_file_path}'")
