# Importing necessary libraries
import os
import pandas as pd
#initializing necessary variables
folder = "monthly_sales"
dataframe_list = []

# Create a list of dataframes of each file
for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    df = pd.read_excel(filepath)
    dataframe_list.append(df)

# Merge them as one dataframe with "Date" column as primary key
merged_df = pd.concat(dataframe_list, ignore_index= 0)

# Convert Date Column of merged dataframe to Datetime datatype
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

# Rearrange merged dataframe
merged_df = merged_df.sort_values(by="Date", ascending=True).reset_index(drop=True)
merged_df.to_excel("2024_Year_Sales.xlsx", index= False)