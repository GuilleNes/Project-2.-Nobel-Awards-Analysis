import pandas as pd
import os
from dotenv import load_dotenv
from pandas import json_normalize
import json
import sys
import re




# Function for extracting values from the chaos column.

# This one is just for the Award Year
def get_year(a, b):
    append_data = []
    for i in range(len(dict_nobel)):
        append_data.append(dict_nobel[i][0][b])
    df1[a] = append_data
    return 

# This one for getting the info of other fields classified by language
def get_info(a, b):
    append_data = []
    for i in range(len(dict_nobel)):
        append_data.append(dict_nobel[i][0][b]["en"])
    df1[a] = append_data
    return 

#renaming the columns
def rename_columns(column, newname):
    df1.rename(columns = {column:newname}, inplace = True)
    return
  
# Dropping columns
def drop_column(datfr, column):
    datfr = datfr.drop([column], axis = 1)
    return

# Calculating the age of each Nobel awarded

def getting_birth (ds, column):
    pattern = "(\d{4})"
    ds[column] = ds[column].apply(lambda x: re.findall(pattern, str(x))).apply(lambda x: ' '.join(x))
    return

#  Creating a new column with the age of the awarded

def getting_age (ds):
    ds["Age"] = ds["AwardYear"].astype(int) - ds["Birth"].astype(int) 
    return

# We delete some of the rows with missing data (the ones with more than one missing value)
def drop_nan(df):
    dfr.dropna(axis=0, inplace=True, thresh=6)
    df1.reset_index(drop=True, inplace=True)
    return
# This function is used for sort and reset the df.
def sort_reset(dfr):
    dfr.sort_values(by = ["AwardYear"], inplace = True)
    dfr.reset_index(drop=True, inplace=True)
    return
    