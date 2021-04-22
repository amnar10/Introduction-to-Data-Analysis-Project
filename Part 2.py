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
list_4star_ratings=['4 star ratings']
list_3star_ratings=['3 star ratings']
list_2star_ratings=['2 star ratings']
list_1star_ratings=['1 star ratings']

total_ratings_np= np.array(android_games[list_total_ratings])
five_star_ratings_np=np.array(android_games[list_5star_ratings])
four_star_ratings_np=np.array(android_games[list_4star_ratings])
three_star_ratings_np=np.array(android_games[list_3star_ratings])
two_star_ratings_np=np.array(android_games[list_2star_ratings])
one_star_ratings_np=np.array(android_games[list_1star_ratings])


percentage_5_star = five_star_ratings_np / total_ratings_np * 100
print(percentage_5_star)

percentage_4_star = four_star_ratings_np / total_ratings_np * 100
print(percentage_4_star)

percentage_3_star = three_star_ratings_np / total_ratings_np * 100
print(percentage_3_star)

percentage_2_star = two_star_ratings_np / total_ratings_np * 100
print(percentage_2_star)

percentage_1_star = one_star_ratings_np / total_ratings_np * 100
print(percentage_1_star)

np.mean(percentage_1_star)
print(np.mean(percentage_1_star))

np.mean(percentage_2_star)
print(np.mean(percentage_2_star))

np.mean(percentage_3_star)
print(np.mean(percentage_3_star))

np.mean(percentage_4_star)
print(np.mean(percentage_4_star))

np.mean(percentage_5_star)
print(np.mean(percentage_5_star))

import matplotlib.pyplot as plt
plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '5star', '4star', '3star', '2star', '1star'
sizes = [70, 12, 6, 3, 9]


fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

























