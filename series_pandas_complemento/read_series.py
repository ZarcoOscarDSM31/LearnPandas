import pandas as pd

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()

#RESULT
#print(f'\n\nContenido de la serie: \n{nba_players}')

#TYPE
#print(type(nba_players))

#DESCRIBE
#print(nba_players.describe())

#HEAD
#print(nba_players.head())

#print(nba_players.head(10))

#TAIL
#print(nba_players.tail())

print(nba_players.tail(10))