## Welcome to Data Cleaner

# Import Libraries
import pandas as pd 
import numpy as np 

# Identify missing values
missing_values = ["n/a", "na", "--", "-", "/"] 
# If missing values in your data is a symbol not listed here, feel free to add those symbols by uncommenting line below
# missing_values = missing_values + ["dw"]
# Copy paste above line with more symbols if needed

# Read Data (replace yourdata with your csv file)
yourdata = "C:\DEV\MLpython\MyDS-MLProjects\Data Cleaner\example.csv"

df = pd.read_csv(yourdata, na_values = missing_values) # Replace yourdata with "yourfile.csv", make sure to data file in same folder
print(df.head(7))

# Detecting numbers in string type columns, turn to NaN
i=0
for row in df['Team']:
    try:
        int(row)
        df.loc[i, 'Team']="Unknown"
    except ValueError:
        pass
    i+=1

print(df.head(7))
# Detecting strings in number type columns, turn to "Unknown"
i=0
for row in df['Year']:
    try:
        int(row)
    except ValueError:
        df.loc[i, 'Year']=np.nan
        pass
    i+=1

# Preview New Data Frame
print(df.head(7))
# Uncomment line below to save new Data Frame to relative location. Feel free to change the name from result!
# df.to_csv("result.csv")





