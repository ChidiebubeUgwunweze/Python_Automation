#import necessary libraries (Pandas)
import pandas as pd

# Convert csv file to a DataFrame
data = pd.read_csv("sales_data_sample.csv", encoding ="latin1")

# Remove unnecessary column(s) 
data.drop('ADDRESSLINE2', axis=1, inplace=True)

# Convert the ORDERDATE column to python's datetime format
data["ORDERDATE"] = pd.to_datetime(data['ORDERDATE'])

# Dropping possible duplicates
data.drop_duplicates(inplace= True)

# Converting columns QTR_ID, MONTH_ID, YEAR_ID into data type iint
data['QTR_ID'] = data['QTR_ID'].astype(int)
data['MONTH_ID'] = data['MONTH_ID'].astype(int)
data['YEAR_ID'] = data['YEAR_ID'].astype(int)

#Total revenue created
total_revenue = data['SALES'].sum()

#Summary by region/country
summary_region = data.groupby("COUNTRY", as_index= False)["SALES"].sum()

new_row = {"COUNTRY": "TOTAL SALES",
           "SALES": summary_region["SALES"].sum()}

summary_region.loc[len(summary_region)] = new_row 
summary_region.to_excel("Summary_by_Country.xlsx")

# Converting the cleaned DataFrame to a cleaned csv file
data.to_csv("cleaned_sales_data_sample.csv", index=False)