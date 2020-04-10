# NBA Win Percentage Predictor
### _Multiple regression model predicting season win percentage of an NBA team based on its statistics_

## Goal
Create a model to predict final season win percentage for an NBA team based on its current per-game statistics

## Data Cleaning/Preprocessing
__Basic NBA statistics for the years 1996-2019__
1. Used Selenium to scrape [stats.nba.com](https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1 "NBA Stats Official Site")
   * Removed endline character and team rank from each row (using a regular expression); kept only columns of interest
   * Created dataframe from list of lists, where the first sub-list was the column names and the rest of the sub-lists were one team's          stats from that season
   * Inserted 'Season' column for each row to keep track of NBA season
   * Concatenated each season's stats to the previous season
   * Renamed columns that contained non-alphabetic characters
2. Log Transformations and Normalization
   * Ran log transformations using NumPy on variables deemed necessary due to the distribution shape of the variable (can possibly be          explained by more recent trends in basketball, i.e. dramatic increase in three-point shots since 2014)
   * Normalized all of the variables (including those that were log transformed) so that they would all be on the same scale given how          they differ
   
## Exploratory Data Analysis
1. Correlation heatmap of basketball statistics
  <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/heatmap.png"></p>

2. Scatter matrix and histograms of the distribution shapes of all of the variables — normal vs. skewed (snippet of whole diagram)
  <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/scatter_matrix.png"></p>
