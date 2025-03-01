import pandas as pd

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()

single_value = nba_players.iloc[3]
print(f'Funcion GET_VALUE: {single_value}')

multi_values = nba_players.iloc[:100].tolist()
print(multi_values)
print(len(multi_values))
print(type(multi_values))


multi_values_2 = nba_players.iloc[:100]
print(type(multi_values_2))