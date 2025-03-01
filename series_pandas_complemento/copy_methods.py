import pandas as pd

nba_players_df = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['Name']).head(5)
nba_players_copy = nba_players_df.squeeze().copy()
nba_players_view = nba_players_df.squeeze()

nba_players_view.iloc[0] = 'UTVT'
nba_players_copy.iloc[0] = 'Lerma'
print(nba_players_df)
print(f'\n{nba_players_copy}')
print(f'\n{nba_players_view}')