import pandas as pd

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()


result_from_a = nba_players.sort_values()
result_from_z = nba_players.sort_values(ascending=False)

print(f'Funcion SORTED: \n{result_from_a}')

print(f'Funcion SORTED: \n{result_from_z}')