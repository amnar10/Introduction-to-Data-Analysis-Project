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

list1np= np.array(android_games[list1])
print(type(list1np))

list2np= np.array(android_games[list2])
print(type(list2np))

np_30_60=list1np + list2np / 2
print(np_30_60)

















