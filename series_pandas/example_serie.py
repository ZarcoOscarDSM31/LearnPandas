import pandas as pd

list_ice_cream = ["chocolate", "vanilla", "strawberry"]
ice_cream_series = pd.Series(list_ice_cream)
print(f'Contenido de la seire: \n{ice_cream_series}')


#Indice personalizado
index = ['a', 'b', 'c']
serie_2 = pd.Series(list_ice_cream, index)

print(f'\n\nEste es el contenido de la serie 2: \n{serie_2}')