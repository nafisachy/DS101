import pandas as pd

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)


# slicing using iloc
df1 = df.iloc[0:4] # when there is : it stops before the end number
print(df1)

# slicing columns in dataframe
df1 = df.iloc[:, 0:2] # 2 columns
print(df1)

# selecting a cell in dataframe
specific_cell_value = df.iloc[2, 3] # column 2 and row 3
print("Specific cell value: ", specific_cell_value)

# boolean conditions
filtered_data = df[df['Age'] > 35].iloc[:, :] # rows where age is greater
print("\nFiltered Data based on Age > 35:\n", filtered_data)

# slicing with loc[]
df_custom = df.set_index('Name')
print(df_custom)

sliced_rows_custom = df_custom.loc['A.B.D Villers': 'S.Smith']
print(sliced_rows_custom)

specific_cell_value = df_custom.loc['V.Kohli', 'Salary']
print("\nValue of the Specific Cell (V.Kohli, Salary):", specific_cell_value)