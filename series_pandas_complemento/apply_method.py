import pandas as pd


def convert_upper(value):
    return value.upper()

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
result = nba_players.apply(convert_upper).head()

print(result)