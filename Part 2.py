import pandas as pd

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

import numpy as np

android_games = pd.read_csv("android-games.csv")
print(android_games.shape)
print(android_games.columns)
print(android_games.head(5))

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

labels = '5star', '4star', '3star', '2star', '1star'
sizes = [70, 12, 6, 3, 9]

fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

top_50=android_games[:50]
print(top_50)
bottom_50=android_games[:-50]
print(bottom_50)

list_top_50=['total ratings']
list_top_50_30day=['growth (30 days)']
list_top_50_60day=['growth (60 days)']
list_bottom_50=['total ratings']
list_bottom_50_30day=['growth (30 days)']
list_bottom_50_60day=['growth (60 days)']

list_top_50_np=np.array(top_50[list_top_50])
list_top_50_30day_np=np.array(top_50[list_top_50_30day])
list_top_50_60day_np=np.array(top_50[list_top_50_60day])
list_bottom_50_np=np.array(bottom_50[list_bottom_50])
list_bottom_50_30day_np=np.array(bottom_50[list_bottom_50_30day])
list_bottom_50_60day_np=np.array(bottom_50[list_bottom_50_60day])

Avg_top50_3060= list_top_50_30day_np + list_top_50_60day_np / 2
Avg_bottom50_3060= list_bottom_50_30day_np + list_bottom_50_60day_np / 2

np.mean(Avg_top50_3060)
print(np.mean(Avg_top50_3060))
np.mean(Avg_bottom50_3060)
print(np.mean(Avg_bottom50_3060))

print(min(Avg_top50_3060))
print(max(Avg_top50_3060))
print(min(Avg_bottom50_3060))
print(max(Avg_bottom50_3060))

np.mean(list_top_50_np)
print(np.mean(list_top_50_np))
np.mean(list_bottom_50_np)
print(np.mean(list_bottom_50_np))

fig,ax=plt.subplots()
ax.scatter(top_50['rank'], top_50['growth (30 days)'])
ax.set_xlabel('Rank')
ax.set_ylabel('Growth (30 days)')
plt.show()

fig,ax=plt.subplots()
ax.scatter(bottom_50['rank'], bottom_50['growth (60 days)'])
ax.set_xlabel('Rank')
ax.set_ylabel('Growth (60 days)')
plt.show()


















