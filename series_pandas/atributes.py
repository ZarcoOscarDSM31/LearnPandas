import pandas as pd

good_students_qualities = ['kind', 'smart', 'determined']
series = pd.Series(good_students_qualities)
print(f'Contenido de la serie: \n{series}\n')

#Tamaño
print(f'El tamaño de la serie es el siguiente: { series.size}\n')

#La serie tiene valores duplicados?
print(f'La serie tiene valores duplicados?: {series.is_unique}\n')

#Información del indice
print(f'Información del indice {series.index}\n')

#INformación del almacenamiento de los valores de la serie
print(f'Información del almacenamiento de los valores de la serie {series.values}\n')

#Información del tipo de los valores de la serie
print(f'Información del tipo de los valores de la serie {type(series.values)}\n')