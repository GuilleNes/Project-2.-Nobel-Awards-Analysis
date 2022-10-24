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
    datfr = datfr.drop([column], axis = 1, inplace= True)
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
    

# Deleting empty elements in a list from webscrapping   
def compact(lst):
    return list(filter(None, lst))

# -----------------------------------------------------------------


# Cleaning the data from webscrapping

def compact(lst):
    return list(filter(None, lst))

#Regex on the columns for the GDP

def n_column(df_, column1, columnn):  
    pattern = "\d{1,3}[\,\.]\d{1,3}[\,\.]\d{1,3}|\d{1,3}[\,\.]\d{1,3}"
    df_[columnn] = df_[column1].apply(lambda x: re.findall(pattern, str(x)))
    return

#------------------------------------------------------------------
#Cleaning the PISA report

def delete_rows(column, value):
    df3.drop(df3.loc[df3[column]==value].index, inplace=True)
    return  

# Deleting the rows by countries we are not interested in

def delete_rows_country(column):
    for i in Countries:
        if i not in column:
            df3.drop(df3.loc[df3[column]==i].index, inplace=True)
    df3.reset_index(drop=True, inplace=True)
    return
         
Countries= ['Albania', 'Algeria', 'Argentina', 'Armenia', 'Azerbaijan', 'Bahrain', 'Belize', 'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Chad', 'Chile', 'Colombia', 'Comoros', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Ethiopia', 'Gabon', 'Georgia', 'Ghana', 'Greece', 'Guatemala', 'Guyana', 'Honduras', 'Hungary', 'Indonesia', 'Iran, Islamic Rep.', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Latvia', 'Lebanon', 'Lesotho', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Macedonia, FYR', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritius', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nicaragua', 'Niger', 'Oman', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Qatar', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Slovak Republic', 'Slovenia', 'South Africa', 'Swaziland', 'Syrian Arab Republic', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'Venezuela, RB', 'Vietnam', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']

lis = ['Australia','Belgium','Brazil','Canada','Denmark','Estonia','Finland', 'France','Germany','Greece','Ireland','Italy', 'Japan','Korea, Rep.''Mexico','Morocco','Netherlands' ,'New Zealand', 'Norway', 'Portugal', 'Russian Federation','South Africa',  'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States']     

