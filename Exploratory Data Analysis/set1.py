import numpy as np
import pandas as pd

from scipy.stats import trim_mean


# Loading data
data = pd.read_csv('state.csv')

# Check data type
print('Type: ', type(data), '\n\n')

# Print top 10 records
print('Head -- \n', data.head(10))

# Print last 10 records
print('\n\n Tail -- \n', data.tail(10))

# Adding column to the dataframe
data['PopulationInMillions'] = data['Population']/1000000
print(data.head(5))

# Data Description
print(data[['Population', 'Murder.Rate']].describe())

# Data Information
data.info()

# Rename column heading
data.rename(columns={'Murder.Rate': 'MurderRate'}, inplace=True)
print(list(data))


# Calculating Mean
population_mean = data.Population.mean()
print("Population Mean: ", population_mean)

murderRate_mean = data.MurderRate.mean()
print("MurderRate Mean: ", murderRate_mean)


# Trimmed Mean:
# Mean after discarding top and bottom 10% values, eliminating outliers

population_TM = trim_mean(data.Population, 0.1)
print("Population trimmed mean: ", population_TM)

murderRate_TM = trim_mean(data.MurderRate, 0.1)
print("MurderRate trimmed mean: ", murderRate_TM)


# Weighted Mean
# Murder rate weighed as per the state population

murderRate_WM = np.average(data.MurderRate, weights=data.Population)
print("MurderRate weighted mean: ", murderRate_WM)


# Median
population_median = data.Population.median()
print("Population median: :", population_median)

murderRate_median = data.MurderRate.median()
print("MurderRate median: ", murderRate_median)