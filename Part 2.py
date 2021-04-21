import pandas as pd

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

import numpy as np

android_games = pd.read_csv("android-games.csv")
print(android_games.shape)
print(android_games.columns)
print(android_games.head(5))

list=['rank', 'title', 'installs', 'paid', 'category']
list1=['growth (30 days)']
list2=['growth (60 days)']
list3=['title', 'total ratings', 'average rating', 'paid']

print(android_games[list1].head())

list_30_day_np= np.array(android_games[list1])
print(type(list_30_day_np))

list_60_day_np= np.array(android_games[list2])
print(type(list_60_day_np))

np_30_60= list_30_day_np + list_60_day_np / 2
print(np_30_60)

list_total_ratings=['total ratings']
list_5star_ratings=['5 star ratings']

total_ratings_np= np.array(android_games[list_total_ratings])
five_star_ratings_np=np.array(android_games[list_5star_ratings])

percentage_5_star = five_star_ratings_np / total_ratings_np * 100
print(percentage_5_star)






















