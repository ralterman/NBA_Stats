# NBA Win Percentage Predictor
### _Multiple regression model predicting season win percentage of an NBA team based on its statistics_

## Goal
Create a model to predict final season win percentage for an NBA team based on its current per-game statistics

## Data Cleaning/Preprocessing
__Basic NBA statistics for the years 1996-2019__
__Variables: WIN%, PTS, FGM, FGA, FG%, 3PM, 3PA, 3P%, FTM, FTA, FT%, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF__
1. Used Selenium to scrape [stats.nba.com](https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1 "NBA Stats Official Site")
   * Removed endline character and team rank from each row (using a regular expression); kept only columns of interest
   * Created dataframe from list of lists, where the first sub-list was the column names and the rest of the sub-lists were one team's          stats from that season
   * Inserted 'Season' column for each row to keep track of NBA season
   * Concatenated each season's stats to the previous season
   * Renamed columns that contained non-alphabetic characters
2. Log Transformations and Normalization
   * Ran log transformations using NumPy on variables deemed necessary due to the distribution shape of the variable and/or OLS p-value,        see below (can possibly be explained by more recent trends in basketball, i.e. dramatic increase in three-point shots since 2014)
   * Normalized all of the variables (including those that were log transformed) so that they would all be on the same scale given how          they differ
   
## Exploratory Data Analysis
1. Correlation heatmap of basketball statistics
  <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/heatmap.png"></p>

2. Scatter matrix and histograms of the distribution shapes of all of the variables — normal vs. skewed (snippet of whole diagram)
  <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/scatter_matrix.png"></p>

## OLS Tables
1. Began by creating Ordinary Least Squares (OLS) regression table on all variables prior to any transformations
2. Followed that up by creating an OLS table with every variable logarithmically transformed
3. Finally, made an OLS table only logarithmically transforming the variables that had a lower p-value when logarithmically transformed
  <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/ols_tables.png"></p>

4. Initial Refinement
    * Removed variables with high p-values
    * R<sup>2</sup> = 0.844
    * Checked for multicolinearity between variables (where variance inflation factor is greater than 5)
    <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/ols_tables2.png"></p>

5. Second Refinement
    * Removed one variable from each of the multicolinear pairs and ran OLS again
    * P-values are all well below α = 0.05
    * Appears to no longer be multicolinearity between variables
    * P(F-statistic) = 6.88e<sup>-107</sup>
    <p align="center"><img src="https://github.com/ralterman/nba_win_percentage_predictor/blob/master/images/ols_tables3.png"></p>
