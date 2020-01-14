import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

headers = {'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com', 'x-rapidapi-key': '29234948damsh7f710123ce5be4ap1d448bjsnfc10e145c960'}

years_list = ['2015', '2016', '2017', '2018']
league_name = 'standard'

# Get games by league and year
def get_gameId(years, league, parameters):
    all_games = {}
    for year in years:
        games = []
        base_url = 'https://api-nba-v1.p.rapidapi.com/games/league/' + league + '/' + year
        response = requests.get(base_url, headers=parameters)
        data = response.json()
        each_game = data['api']['games']
        for match in each_game:
            gameId = match['gameId']
            games.append(gameId)
        all_games[year] = games
    return all_games

# get_gameId(years_list, league_name, headers)

gameId_dict = get_gameId(years_list, league_name, headers)

def get_statistics(years, parameters):
    df_list = []
    for season in gameId_dict:
        game_stats = []
        for id in gameId_dict[season]:
            base_url2 = 'https://api-nba-v1.p.rapidapi.com/statistics/games/gameId/' + id
            response2 = requests.get(base_url2, headers=parameters)
            data2 = response.json()
            statistics = data2['api']['statistics']
            for team_stats in statistics:
                game_stats.append(team_stats)
        df = pd.DataFrame(game_stats)
        df_list.append(df)
        return df_list

stats_dfs = get_statistics(years_list, headers)
