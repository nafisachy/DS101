import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

from scipy.stats import trim_mean

data = pd.read_csv('state.csv')

# Adding column to the dataframe
data['PopulationInMillions'] = data['Population']/1000000
print(data.head(5))

# Rename column heading
data.rename(columns={'Murder.Rate': 'MurderRate'}, inplace=True)
print(list(data))


# Visualizing Population per million

# Plot Population in Millions
fig, ax1 = plt.subplots()
fig.set_size_inches(15, 9)

colors = plt.cm.viridis(np.linspace(0, 1, len(data['State'])))

ax1 = sns.barplot(x="State", y="PopulationInMillions", data=data.sort_values('MurderRate'), palette='Set2', hue='State')


ax1.set(xlabel='States', ylabel='Population in Millions')
ax1.set_title('Population in Millions by State', size=20)


plt.xticks(rotation=-90)
# plt.show()



# Standard Deviation- on average how far each value lies from the mean
Population_std = data.Population.std()
print("Population std", Population_std)

MurderRate_std = data.MurderRate.std()
print("MurderRate std : ", MurderRate_std)


# Variance- on average how far each value lies from each other and the mean
Population_var = data.Population.var()
print("\nPopulation var: ", Population_var)

MurderRate_var = data.MurderRate.var()
print("MurderRate var", MurderRate_var)


# Inter Quartile Range
population_IQR = data.Population.describe()['75%'] - data.Population.describe()['25%']
print("\nPopulation IQR: ", population_IQR)

murderRate_IQR = data.MurderRate.describe()['75%'] - data.MurderRate.describe()['25%']
print("MurderRate IQR: ", murderRate_IQR)


# Mean Absolute Deviation MAD
# data['Population'] = data['Population'].astype(int)
# mad = stats.median_abs_deviation(data)
# Population_mad = data.Population.mad
# print("\nPopulation mad: ", Population_mad)
#
# MurderRate_mad = data.MurderRate.mad
# print("MurderRate mad: ", MurderRate_mad)