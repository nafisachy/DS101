import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Titanic-Dataset.csv')
df.head()

# Inspection and Exploration
df.duplicated()

# information
df.info()

# categorical col
cat_col = [col for col in df.columns if df[col].dtype == 'object']
print('Categorical columns :', cat_col)

# numerical col
num_col = [col for col in df.columns if df[col].dtype != 'object']
print('Numerical columns :', num_col)

# total number of unique values in categorical col
df[cat_col].nunique()

# 50 unique tickets
print(df['Ticket'].unique()[:50])

# Drop
df1 = df.drop(columns=['Name', 'Ticket'])
print(df1.shape)

# Handle missing data
round((df1.isnull().sum()/df1.shape[0])*100, 2)

df2 = df1.drop(columns='Cabin') # drop column
df2.dropna(subset=['Embarked'], axis=0, inplace=True) # drop null values
print(df2.shape)


# mean imputation
df3 = df2.fillna(df2.Age.mean())
df3.isnull().sum()

# box plot to handle outlier
plt.boxplot(df3['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
# plt.show()

# calculate summary stats
mean = df3['Age'].mean()
std = df3['Age'].std()

# lower and upper bounds
lower_bound = mean - std*2
upper_bound = mean + std*2

# print('Lower Bound :', lower_bound)
# print('Upper Bound :', upper_bound)

# drop outliers
df4 = df3[(df3['Age'] >= lower_bound) & (df3['Age'] <= upper_bound)]

X = df3[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
Y = df3['Survived']

# Initializing the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X

# statistical parameters for each of the data and transforming
x1[num_col_] = scaler.fit_transform(x1[num_col_])
print(x1)