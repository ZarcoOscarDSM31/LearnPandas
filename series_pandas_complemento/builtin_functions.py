import pandas as pd

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
nba_players_age = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['AGE']).squeeze()

print(f'Nombre de los jugadores:\n{nba_players}')
print(f'\nEdad de los jugadores: \n{nba_players_age}')

#LEN
print(f'Funcion LEN: \n{len(nba_players)}')

#TYPE
print(f'Funcion TYPE: \n{type(nba_players)}')

#SORTED
print(f'Funcion SORTED: \n{sorted(nba_players_age)}')

#MAX
print(f'Funcion MAX: \n{max(nba_players_age)}')

#MIN
print(f'Funcion MIN: \n{min(nba_players_age)}')

