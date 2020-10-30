import pandas as pd
import numpy as np
#from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('ggplot')

#read the csv into a pandas dataframe
df = pd.read_csv('/Users/raffi/Desktop/galvanize/capstone_1/data/games.csv', delimiter = ',')

#dropping duplicated ids in dataframe
df.drop_duplicates(subset = ['id'], inplace = True)

#update moves column from string to list for future analysis
df.moves = df.moves.apply(lambda x: x.split(' '))

#categorizing according to time format
df['game_time'] = df['increment_code'].str.split('+').str[0].astype(int)
df['increment'] = df['increment_code'].str.split('+').str[1].astype(int)

#categorizing games by time increments - rapid, blitz, bullet, classical
def game_category(val):
    if val <= 3:
        return 'bullet'
    elif val <= 10:
        return 'blitz'
    elif val < 60:
        return 'rapid'
    elif val >= 60:
        return 'classical'
    else:
        return 'other'

df['game_category'] = df['game_time'].apply(game_category)

#categorize rating scales
def rating_category(val):
    if val < 800:
        return 'G'
    elif val < 1000:
        return 'F'
    elif val < 1200:
        return 'E'
    elif val < 1400:
        return 'D'
    elif val < 1600:
        return 'C'
    elif val < 1800:
        return 'B'
    elif val < 2000:
        return 'A'
    elif val < 2200:
        return 'Expert'
    elif val < 2400:
        return 'NM'
    elif val > 2400:
        return 'SM'

df['white_rating_cat'] = df['white_rating'].apply(rating_category)
df['black_rating_cat'] = df['black_rating'].apply(rating_category)

#new column for rating differential
df['rating_differential'] = abs(df['white_rating'] - df['black_rating'])


#frequency of top 20 first moves

#top openings

#win probability of top openings

#average moves of openings

#turns by rating group


#plot 1 - rating distribution by white and black
fig, ax = plt.subplots(1,1, figsize = (10,4))
colors = {'white': 'yellow', 'black': 'blue', 'draw': 'green'}
color = ['yellow', 'blue', 'green']
ax.scatter(df.white_rating, df.black_rating, s = 2, c = df.winner.map(colors), label = colors, alpha = 0.3)
ax.set_xlabel('white rating')
ax.set_ylabel('black rating')
#how to get legend to be color of dot + label like white, blue, grey


#new data frame for openings
openings = df.groupby(['opening_name', 'winner'])['id'].count()
openings = pd.DataFrame(openings).reset_index()
openings_df = openings.pivot(index = 'opening_name', columns = 'winner', values = 'id')
openings_df['total_count'] = openings_df['white'] + openings_df['black'] + openings_df['draw']
openings_df['black_percent'] = openings_df['black'] / openings_df['total_count']
openings_df['white_percent'] = openings_df['white'] / openings_df['total_count']
openings_df['draw_percent'] = openings_df['draw'] / openings_df['total_count']
openings_df.sort_values(by = 'total_count', ascending = False, inplace = True)

#plot to show winning percentage by white and black for top 10 openings
#need to update labels and format
fig, ax = plt.subplots(1,1, figsize = (10,6))
x_pos = [i for i in reversed(openings_df.index[0:10])]
wp = np.array(openings_df['white_percent'][0:10])
bp = np.array(openings_df['black_percent'][0:10])
dp = np.array(openings_df['draw_percent'][0:10])
ax.barh(x_pos, wp, color = 'white')
ax.barh(x_pos, bp, color = 'black', left = wp)
ax.barh(x_pos, dp, color = 'blue', left = wp + bp)

