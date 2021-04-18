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

missing_val = vaccinations_country.fillna(0)
print(missing_val)

vaccinations_manufacturer = pd.read_csv("country_vaccinations_by_manufacturer.csv")
print(vaccinations_manufacturer.head(), vaccinations_manufacturer.shape)

dropping_duplicates = vaccinations_country.drop_duplicates()
print(dropping_duplicates.shape)

dropping_duplicates = vaccinations_manufacturer.drop_duplicates()
print(dropping_duplicates.shape)

merged_data = pd.merge(vaccinations_country,vaccinations_manufacturer,on='date')
print(vaccinations_country.shape, vaccinations_manufacturer.shape)
print(merged_data.shape)
print(merged_data)

merged_data = merged_data.sort_values("country")
print(merged_data.head())

merged_data [ (merged_data["vaccine"] == "pfizer") & (merged_data["vaccine"] == "Sinovac") & (merged_data["vaccine"] == "Moderna") & (merged_data["vaccine"] == "AstraZeneca")]

print(merged_data.head())

merged_index_loc=merged_data.set_index("country")
print(merged_index_loc)

merged_index_loc["Afghanistan":"Zimbabwe"]
print(merged_index_loc)