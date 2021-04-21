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
list1=['title','growth (30 days)','growth (60 days)',]
list2=['title', 'total ratings', 'average rating', 'paid']

print(android_games[list].head())
print(android_games[list1].head())
print(android_games[list2].head())


















