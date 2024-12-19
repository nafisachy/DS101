import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)

# using isnull() function
print(df.isnull())

# filling missing value
print(df.fillna(0))

# using dropna() function
print(df.dropna())

dict1 = {'name': ['aparna', 'pankaj', 'sudhir', 'Geeku'],
         'degree': ['MBA', 'BCA', 'M.Tech', 'MBA'],
         'score': [90, 40, 80, 98]}

df1 = pd.DataFrame(dict1)
print(df1)

# iterating over rows using iterrows() function
for i, j in df1.iterrows():
    print("\n", i, j)
    print()

columns = list(df1)

for i in columns:

    # printing the third element of the column
    print(df1[i][2])