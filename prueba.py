import pandas as pd
print('no se que hago.')


df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

if df['A'].sum() > 5:
    if df['B'].mean() > 4:
        print('La suma de A es mayor que 5 y la media de B es mayor que 4')
    else:
        print('La suma de A es mayor que 5 pero la media de B no es mayor que 4')
