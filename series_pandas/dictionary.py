import pandas as pd

kids_gifts = {
    'videogames' : 'xbox',
    'books' : 'The Lord of the Rings',
    'music' : 'The Beatles'
}

kids_gifts_series = pd.Series(kids_gifts)
print(f'Contenido de la serie: \n{kids_gifts_series}')