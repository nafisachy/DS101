import pandas as pd

# Calling dataframe constructor
df = pd.DataFrame()
print(df)

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'Is', 'Portal', 'For', 'Geeks']

# Calling Dataframe constructor on list
df = pd.DataFrame(lst)
print(df)

# Reading the CSV file
df = pd.read_csv('Iris.csv')

# Printing top 5 rows
print(df.head())

# Applying filter function
print(df.filter(["Species", "SepalLengthCm"]).head())

# Applying sorting
print(df.sort_values("SepalLengthCm",axis=0, ascending=True))

# Grouping:
# Splitting is a process in which you split data into group by applying some conditions on datasets
# Applying is a process in which you apply a function to each group independently
# Combining is a process in which you combine different datasets after applying groupby and results into a data structure

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi', 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
         'Age': [27, 24, 22, 32, 33, 36, 27, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh' ],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
# df = pd.DataFrame(data1)
# print("Original DataFrame")
df = pd.DataFrame(data1)
print(df)

# select two columns
print(df[['Name', 'Qualification']])

# Applying groupby() function to group the data on Name value
gk = df.groupby('Name')

# Let's print the first entries in all the group formed
print(gk.first())

# Applying function to group:
# Aggregation is a process in which you compute a summary statistic about each group, like computing group sums or means
print(gk.aggregate({"Age": ["sum"]}))

# Transformation is a process in which you perform some group-specific computations and return a like-indexed.
# Ex- Filling NAs within groups with a value
# Filtration is a process in which you discard some groups, according to a group-wise computation that evaluates True or False
# Ex- filtering out data based on the group sum or mean

# Define a dictionary containing employee data
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32]}

# Define a dictionary containing employee data
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert dictionary into dataframe
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)

print(df, "\n", df1)

# Combining series and dataframe
res = pd.concat([df, df1], axis=1)
print(res)

# Merging dataframe
res = pd.merge(df, df1, on='key')  # Merge with a common value
print(res)

# Joining dataframe
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32]}

data2 = {'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=['K0', 'K1', 'K2', 'K3'])
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])  # Does not have K1 in df, so the K1 in the joined table is NA

print(df, "\n", df1)

res = df.join(df1)
print(res)