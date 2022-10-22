import pandas as pd
import os
from dotenv import load_dotenv
from pandas import json_normalize
import json
import requests


url = 'http://api.nobelprize.org/2.1/laureates?limit=1000&sort=asc&format=json&csvLang=en'
parameters = {'accept': 'application/json'}
response = requests.get(url).json()


#Setting the columns of the df and keeping those needed

df1 = df[["gender", "nobelPrizes", "knownName.en", "birth.place.country.en", "birth.date"]]
dict_nobel = df1["nobelPrizes"]

#We use some functions to clean the nobelPrizes column creating a nwe column, where all the usefull info is

#First we get the award year

get_year("AwardYear", "awardYear")

#Next we get the category of the prize

get_info("Category", "category")

#As curiosity, but not a needed field, we clean the motivation of the work that diserved the award.

get_info("Theme", "motivation")

# We are going to rename the columns

rename_columns("knownName.en", "Name")
rename_columns("birth.place.country.en", "Country")
rename_columns("birth.place.country.en", "Birth")




