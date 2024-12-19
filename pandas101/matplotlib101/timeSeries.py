import pandas as pd
import matplotlib.pyplot as plt

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday']

calories = [1670, 2011, 1853, 2557,
            1390, 2118, 2063]

df_days_calories = pd.DataFrame({'days': days, 'calories': calories})

print(df_days_calories)
df_days_calories.plot('days', 'calories')
plt.show()

subjects = ['Math', 'English', 'History',
            'Chem', 'Geo', 'Physics', 'Bio', 'CS']

stress = [9, 3, 5, 1, 8, 5, 10, 2]

grades = [15, 10, 7, 8, 11, 8, 17, 20]

df1 = pd.DataFrame(list(zip(stress, grades)),  # combine tuples, convert to list
                   index=subjects,
                   columns=["Stress", "Grades"])

df1.plot()
plt.show()