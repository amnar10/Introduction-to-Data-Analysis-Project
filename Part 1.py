import pandas as pd

vaccinations_country=pd.read_csv("country_vaccinations.csv")
print(vaccinations_country.head(), vaccinations_country.shape)

import pandas as pd

vaccinations_manufacturer=pd.read_csv("country_vaccinations_by_manufacturer.csv")
print(vaccinations_manufacturer.head(), vaccinations_manufacturer.shape)

import pandas as pd

vaccinations_country=pd.read_csv("country_vaccinations.csv")
print(vaccinations_country.head(), vaccinations_country.shape)
vaccinations_country
missing_val=vaccinations_country.isnull()
print(missing_val)
