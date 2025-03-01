import pandas as pd

nba_players = pd.read_csv(r'C:\Users\oscar\OneDrive\Documents\Universidad\octavo\prog\nba_players_a.csv', sep=',', usecols=['DRtg']).squeeze()
some_values = nba_players.iloc[:5]

#ADDITION
addition_1 = some_values + 10
addition_2 = some_values.add(10)

print(f'Realización de una suma: ')
print(some_values)
print(addition_1)
print(addition_2)

print(f'Realización de una resta: ')
subtract_1 = some_values - 10
subtract_2 = some_values.sub(10)
print(subtract_1)
print(subtract_2)

print(f'Realización de una multiplicación: ')
multiply_1 = some_values * 2
multiply_2 = some_values.mul(2)

print(multiply_1)
print(multiply_2)


print(f'Realización de una división: ')
division_1 = some_values / 10
division_2 = some_values.div(10)


print(division_1)
print(division_2)