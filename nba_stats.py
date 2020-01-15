import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import requests
from selenium import webdriver
import re
import time

pd.set_option('display.max_columns', 30)


seasons = ['1996-97', '1997-98', '1999-00', '2000-01', '2001-02', '2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08',
            '2008-09', '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19']


def get_data(seasons_list):
    statistics = pd.DataFrame()
    for season in seasons_list:
        url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=' + season + '&SeasonType=Regular%20Season&PerMode=Totals'
        driver = webdriver.Chrome(r"/Users/Robert/Downloads/chromedriver")
        driver.get(url)
        time.sleep(3)
        table = driver.find_element_by_class_name('nba-stat-table__overflow')
        remove_endline = table.text.split('\n')
        row_to_string = ' '.join(remove_endline)
        split_lines = re.sub(r'\s\d{1,2}\s([A-Z])', r'\n\1', row_to_string)
        separate_teams = split_lines.split('\n')
        table_list = []
        for row in separate_teams:
            split_stats = row.split()
            table_list.append(split_stats[-27:])
        df = pd.DataFrame.from_records(table_list[1:], columns = table_list[0])
        df.insert(0, 'SEASON', season)
        statistics = pd.concat([statistics, df], ignore_index = True)
        driver.close()
    return statistics

statistics_df = get_data(seasons)
statistics_df

statistics_df.to_csv('nba_statistics.csv', index=False)
stats_df = pd.read_csv('nba_statistics.csv')

plt.figure(figsize=(30,40))
sns.heatmap(stats_df.corr(), cmap="YlGnBu", annot=True)
