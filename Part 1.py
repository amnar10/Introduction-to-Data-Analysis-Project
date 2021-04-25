import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
import numpy as np

vaccinations_country = pd.read_csv("country_vaccinations.csv")
print(vaccinations_country.head(), vaccinations_country.shape)
vaccinations_manufacturer = pd.read_csv("country_vaccinations_by_manufacturer.csv")
print(vaccinations_manufacturer.head(), vaccinations_manufacturer.shape)

missing_val = vaccinations_country.isnull().sum()
print(missing_val)

dropping_duplicates = vaccinations_country.drop_duplicates()
print(dropping_duplicates.shape)
dropping_duplicates = vaccinations_manufacturer.drop_duplicates()
print(dropping_duplicates.shape)






