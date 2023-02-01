import re
import pandas as pd


# Function for extracting values from the chaos column.

def get_year(dic, df, a, b):
    df[a] = [dic[i][0][b] for i in range(len(dic))]
    return

# This one for getting the info from other fields classified by language
def get_info(df, dic, a, b):
    df[a] = [dic[i][0][b]["en"] for i in range(len(dic))]
    return

#renaming the columns
def rename_columns(df, column, newname):
    df.rename(columns = {column:newname}, inplace = True)
    return
  
# Dropping columns
def drop_column(df, column):
    df = df.drop([column], axis = 1, inplace= True)
    return

# Calculating the age of each Nobel awarded

def getting_birth (df, column):
    pattern = "(\d{4})"
    df[column] = df[column].apply(lambda x: re.findall(pattern, str(x))).apply(lambda x: ' '.join(x))
    return

#  Creating a new column with the age of the awarded

def getting_age (df):
    df["Age"] = df["AwardYear"].astype(int) - df["Birth"].astype(int) 
    return

# We delete some of the rows with missing data (the ones with more than one missing value)
def drop_nan(df):
    df.dropna(axis=0, inplace=True, thresh=6)
    df.reset_index(drop=True, inplace=True)
    return

# This function is used for sort and reset the df.
def sort_reset(df, column):
    df.sort_values(by = [column], inplace = True)
    df.reset_index(drop=True, inplace=True)
    return
    

# Deleting empty elements in a list from webscrapping   
def compact(lst):
    return list(filter(None, lst))

# -----------------------------------------------------------------


# Cleaning the data from webscrapping

def compact(lst):
    return list(filter(None, lst))

#Regex on the columns for the GDP

def n_column(df, column1, columnn):  
    pattern = "\d{1,3}[\,\.]\d{1,3}[\,\.]\d{1,3}|\d{1,3}[\,\.]\d{1,3}"
    df[columnn] = df[column1].apply(lambda x: re.findall(pattern, str(x)))
    return

#------------------------------------------------------------------
#Cleaning the PISA report

def delete_rows(df, column, value):
    df.drop(df.loc[df[column]==value].index, inplace=True)
    return  

# Deleting the rows by countries we are not interested in

def delete_rows_country(df, column, lista):
    for i in df[column]:
        if i not in lista:
            df.drop(df.loc[df[column]==i].index, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return 
         
Countries= ['Albania', 'Algeria', 'Argentina', 'Armenia', 'Azerbaijan', 'Bahrain', 'Belize', 'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Chad', 'Chile', 'Colombia', 'Comoros', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Ethiopia', 'Gabon', 'Georgia', 'Ghana', 'Greece', 'Guatemala', 'Guyana', 'Honduras', 'Hungary', 'Indonesia', 'Iran, Islamic Rep.', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Latvia', 'Lebanon', 'Lesotho', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Macedonia, FYR', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritius', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nicaragua', 'Niger', 'Oman', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Qatar', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Slovak Republic', 'Slovenia', 'South Africa', 'Swaziland', 'Syrian Arab Republic', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'Venezuela, RB', 'Vietnam', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']

lis = ['Australia','Belgium','Brazil','Canada','Denmark','Estonia','Finland', 'France','Germany','Greece','Ireland','Italy', 'Japan','Korea, Rep.''Mexico','Morocco','Netherlands' ,'New Zealand', 'Norway', 'Portugal', 'Russian Federation','South Africa',  'Spain', 'Sweden', 'Switzerland', 'United Kingdom', 'United States']     

Countries2= ['India','West Germany','Austrian Empire', 'New Zealand','Southern Rhodesia', 'Guadeloupe Island', 'Brazil','Egypt', 'Romania', 'Northern Ireland', 'British West Indies', 'Crete', 'Venezuela', 'Mexico', 'German-occupied Poland', 'Taiwan','Albania','Schleswig', "nan", 'Nigeria', 'Korea', 'Tibet', 'Burma', 'Saint Lucia', 'British Mandate of Palestine', 'East Timor','Free City of Danzig', 'Gold Coast', 'Iran', 'British Protectorate of Palestine', 'Czechoslovakia','Persia','East Friesland', 'Iceland','Ottoman Empire','French Algeria', 'Liberia','Yemen', 'Pakistan','Belgian Congo','Iraq',   'Bosnia', 'Faroe Islands (Denmark)','Scotland','Tuscany','British India','Russian Empire', 'Hesse-Kassel','Mecklenburg','Schleswig','Ireland','Austria-Hungary','Java, Dutch East Indies','Württemberg','Bavaria', 'Algeria', 'Argentina', 'Armenia', 'Azerbaijan', 'Bahrain', 'Belize', 'Benin', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cameroon', 'Chad', 'Chile', 'Colombia', 'Comoros', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Ethiopia', 'Gabon', 'Georgia', 'Ghana', 'Greece', 'Guatemala', 'Guyana', 'Honduras', 'Hungary', 'Indonesia', 'Iran, Islamic Rep.', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Latvia', 'Lebanon', 'Lesotho', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Macedonia, FYR', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritius', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nicaragua', 'Niger', 'Oman', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Qatar', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Slovak Republic', 'Slovenia', 'South Africa', 'Swaziland', 'Syrian Arab Republic', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'Venezuela, RB', 'Vietnam', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']


# Replacement function for all the column names

def repl(name):
    match = re.search("^\d*(?=\s)", name)
    return match.group(0) if match else name


# Getting tableau plots in Jupyter Notebook

def dynamic_df():
    return pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])