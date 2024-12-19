import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../Exploratory Data Analysis/Iris.csv')
print(df.head())

# How many columns and rows does the dataframe consist of
print(df.shape)

# # Information about the dataset
df.info()

# Description of the dataset (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe())

# Check missing value
print(df.isnull().sum())

# Check duplicates
data = df.drop_duplicates(subset="Species")
print(data)

# Check value count- If the data contains equal amount of rows or no
print(df.value_counts("Species"))


# Comparing Sepal length and width
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

# Comparing Petal Length and width
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', hue='Species', data=df)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()


# Pairplot
sns.pairplot(df.drop(['Id'], axis=1), hue='Species', height=2)
plt.show()

# Handling correlation
data1 = df[['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
print(data1.corr(method='pearson'))

# Heatmaps
sns.heatmap(data1.corr(method='pearson').drop(['Id'], axis=1).drop(['Id'], axis=0), annot=True);
plt.show()

# Handling Outliers
sns.boxplot(x='SepalWidthCm', data=df)
plt.show()

# Removing Outliers

# IQR (Need to dive deeper into this)
Q1 = np.percentile(df['SepalWidthCm'], 25, interpolation='midpoint')

Q3 = np.percentile(df['SepalWidthCm'], 75, interpolation='midpoint')

IQR = Q3-Q1
print('Old Shape: ', df.shape)

# Upper bound
upper = np.where(df['SepalWidthCm'] >= (Q3+1.5*IQR))

# Lower bound
lower = np.where(df['SepalWidthCm'] <= (Q3-1.5*IQR))

# Removing the outlier
df.drop(upper[0], inplace=True)

df.drop(lower[0], inplace=True)

print('New Shape: ', df.shape)

sns.boxplot(x='SepalWidthCm', data=df)
plt.show()