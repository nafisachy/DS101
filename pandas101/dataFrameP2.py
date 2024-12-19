import pandas as pd

# making data frame from csv file
data = pd.read_csv('nba.csv', index_col='Name')

# retrieving row by loc method
first = data.loc['Avery Bradley']
second = data.loc[['R.J. Hunter', 'Amir Johnson']]

# retrieving all rows and some columns by loc method
third = data.loc[:, ['Team', 'Number', 'Position']]

print(first, "\n\n\n", second, "\n\n\n", third)

row2 = data.iloc[:, [1, 2]]
print(row2)