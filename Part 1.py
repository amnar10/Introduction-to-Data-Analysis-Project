import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

vaccinations_country = pd.read_csv("country_vaccinations.csv")
print(vaccinations_country.head(), vaccinations_country.shape)

import pandas as pd

vaccinations_manufacturer = pd.read_csv("country_vaccinations_by_manufacturer.csv")
print(vaccinations_manufacturer.head(), vaccinations_manufacturer.shape)

import pandas as pd

vaccinations_country = pd.read_csv("country_vaccinations.csv")
print(vaccinations_country.head(), vaccinations_country.shape)

vaccinations_country
missing_val = vaccinations_country.isnull()
print(missing_val)

missing_val = vaccinations_country.isnull().sum()
print(missing_val)

vaccinations_manufacturer = pd.read_csv("country_vaccinations_by_manufacturer.csv")
print(vaccinations_manufacturer.head(), vaccinations_manufacturer.shape)

dropping_duplicates = vaccinations_country.drop_duplicates()
print(dropping_duplicates.shape)

dropping_duplicates = vaccinations_manufacturer.drop_duplicates()
print(dropping_duplicates.shape)

concat_data= pd.concat([vaccinations_country, vaccinations_manufacturer])
print(vaccinations_country.shape,vaccinations_manufacturer.shape,concat_data.shape)

print(concat_data.head())

concat_data = concat_data.sort_values("date", ascending=False)
print(concat_data.head())

concat_data = concat_data.sort_values("country", ascending=True)
print(concat_data.head())

concat_data_loc=concat_data.set_index("country")
print(concat_data_loc)

missing_values_filled = concat_data_loc.fillna(0)
print(missing_values_filled)

import numpy as np







