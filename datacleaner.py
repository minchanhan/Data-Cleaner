## Welcome to Data Cleaner

# Import Libraries
import pandas as pd 
import numpy as np 
# For Previews
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

print("All inputs are case sensitive!")
# Identify missing value symbols
missing_values = ["n/a", "na", "-", "/", " "] 
while(True):
    moremissing = input("Enter more missing value symbols from your data (enter STOP to stop): ") # E.g. --
    if(moremissing == "STOP"):
        break
    missing_values = missing_values + [moremissing]

# Read Data (replace yourdata with your csv file)
yourdata = "C:\DEV\example.csv"

# Replace yourdata with "yourfile.csv", make sure to put data file in same folder as script
df = pd.read_csv(yourdata, na_values=missing_values) 

# Preview your data (Visualizations will be implemented soon!)
print(df.head(10)) # Change # of rows if you'd like
print("\n")

# Detecting numbers in string type columns, turn to NaN
while(True):
    strcol = input("Enter STRING type columns (enter STOP to stop): ") # E.g. Strings
    if(strcol == "STOP"):
        break
    elif(not strcol in df.columns):
        print("This isn't a valid column! Remember Case Sensitive!")
        continue
    i=0
    for row in df[strcol]:
        try:
            int(row)
            df.loc[i, strcol]=np.nan
        except ValueError:
            try:
                float(row)
                df.loc[i, strcol]=np.nan
            except ValueError:
                pass
        i+=1

# Detecting strings in number type columns (int or float), turn to NaN
while(True):
    numcol = input("Now enter NUMBER type columns (enter STOP to stop): ") # E.g. Numbers
    if(numcol == "STOP"):
        break
    elif(not numcol in df.columns):
        print("This isn't a valid column! Remember Case Sensitive!")
        continue
    i=0
    for row in df[numcol]:
        try:
            int(row)
        except ValueError:
            try:
                float(row)
            except ValueError:
                df.loc[i, numcol]=np.nan
                pass
        i+=1


# Preview New Data Frame
print(df.head(10))

# Uncomment line below to save new Data Frame to relative location. Feel free to change the name from result!
# df.to_csv("result.csv")





