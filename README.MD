# I'll Be Sicilian You Later!



## Table of Contents
1. Overview
2. Data Set
3. Questions
4. Analysis
5. Conclusion

## Overview

Chess is a two-player strategy board game played on a checkered board with 64 squares in an 8x8 square grid. The game is believed to have originated in India in the 6th century. Since then, chess has evolved into both a sport and a casual game that is enjoyed by millions of people worldwide!

To play chess, each player begins with 16 pieces: one king, one queen, two rooks, two knights, two bishops, and eight pawns. Each piece moves differently, with the most powerful being the queen and the least powerful the pawn. Play involves no hidden information. The objective is to checkmate the opponent's king by placing it under an inescapable threat of capture. 

Chess strategy consists of setting and achieving long-term positioning advantages during the game, while chess tactics concentrate on immediate maneuvering. A game of chess is normally divided into three phases: the opening, typically the first 10 moves, the middlegame, and the endgame. 

## Data Set

<p align="center">
    <img src="images/df_head.png" width='500'/>
</p>

The analysis is based on the Chess Game Dataset (Lichess), which includes data from nearly 20,000 games from a selection of users on Lichess.org. General information about the dataset can be found below:

### General Info:\
Game ID: object\
Rated (T/F): bool\
Start Time: float64\
End Time: float64\
Number of Turns: int64\
Game Status: object\
Winner: object\
Time Increment: object\
White Player ID: object\
White Player Rating: int64\
Black Player ID: object\
Black Player Rating: int64\
All Moves in Standard Chess Notation: object\
Opening Eco (Code for any given opening): object\
Opening Name: object\
Opening Ply (Number of moves in opening phase): int64\

### Cleaning
Most of the columns in the dataset are categorical. I loaded the file (csv format) into a pandas dataframe and performed the following cleaning procedures. A link to a jupyter notebook containing my python code can be found [HERE](chess_EDA_Final.ipynb).

Game IDs: dropped duplicate values\
All Moves in Standard Chess Notation: transformed values from a string into a list\
Player Rating: created a simplified ranking scale for both White and Black players\
Opening Name: created a simplified opening name structure by dropping opening name variations\
Winner: created numerical columns to categorize outcome by white, black, or draw\
Start Time: created new date column in datetime format

## Questions

As an avid chess player, my goals were to perform EDA, calculate the probability of success after each move, and recommend moves based on the outcomes of similar games.

<p align="center">
    <img src="images/huh.gif" width='300'/>
</p>


I quickly realized that I needed to simplify my goals and focused my analysis on answering more basic questions, such as: which opening is most common and is the probability of winning affected by player ranking and piece color.

## Analysis

The dataset included datetime information, which was useful to interpret changes in the game over time. The graph below illustrates how the number of moves per opening (opening_ply) has increased from 2013 to 2017. The graph also shows an increase in average turns per game and player rating over the same time period.


<p align="center">
    <img src="images/openings_turns_ratings_by_year.png" width='400'/>
</p>

The next chart shows the distribution of player ratings by piece color (white and black). Overall, the distribution of players between these two groups was fairly even. 

<p align="center">
    <img src="images/distribution_of_player_ratings_by_piece_color.png" width='400'/>
</p>

<p>
<div align = 'center'>
white rating mean: 1597

black rating mean: 1590
<div>

The graph below provides an alternate visualization; however, this time the distribution is grouped by ranking category.

<p align="center">
    <img src="images/distribution_of_ratings_by_game_and_group.png" width='500'/>
</p>

Next, I wanted to better understand win ratios. According to the dataset, white wins more often than black:

*white win: 50%*\
*black win: 45%*\
*draws: 5%*

Grouping the dataframe by ranking category and piece color provided a better breakdown of wins and losses and whether the overall win ratio was skewed by a select group of players or category of players.

<p align="center">
    <img src="images/white_wins_by_group.png" 
    width='250'/>
    <img src="images/black_wins_by_group.png" 
    width='250'/>
</p>

If you're a beginner, be prepared to lose, a lot. The Master Group wins more frequently than the others. To test the independence of win ratio by group I performed a two-sided t-test between the average win rates between the Masters group and the Novice group. The mean win ratio for Masters and Novices was 68% and 47%, respectively. 

*statistic = 1.579*\
*pvalue = 0.115*


## Part 2

Openings are a very important part of chess strategy. A chess opening is the group of initial moves of the game. These recognized sequences are given names such as the Ruy Lopez or Sicilian Defense. The fundamental strategy of an opening is to develop pieces, control the center, move the king to safety, and maintain pawn structure. 

The dataset included 1,477 unique openings!

<p align="center">
    <img src="images/distribution_of_ratings_by_game_and_group.png" width='700'/>
</p>



Chess Masters win more frequently than Experts, Novices, and Beginners. The graph below highlights the top 20 most frequently used openings by this category.

<p align="center">
    <img src="images/top_20_openings.png" width='400'/>
</p>

<p align="center">
    <img src="images/top_20_openings_master_sorted.png" width='400'/>
</p>

The Sicilian Defense is a strategy by black that creates an unbalanced game with many attacking scenarios. The graph below illustrates the winning percentage of this opening by ranking group.

<p align="center">
    <img src="images/win_rate_of_sicilian.png" width='400'/>
</p>





To expand this concept more broadly, I compared the winning percentages of the rating groups based on whether they were white or black. 




These graphs highlight the first mover advantage, since white pieces move first. Each category won as white more often than as black. The difference in win ratio by Beginners, Novices, Experts, and Masters was 4.9%, 4.8%, 0.3%, and 1.0%, respectively.

To test this I performed a two sample approximate test of population proportions. To set this up I looked at the winning games for beginners playing as white and black. My hypothesis was that a beginner wins an equal amount of games as white and black. In other words, Pbw <= Pbb. 