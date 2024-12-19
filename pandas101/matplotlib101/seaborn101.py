import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Name': ['Mohe', 'Karnal', 'Yrik', 'Jack'],
        'Age': [30, 21, 29, 28],
        'Weight': [215, 225, 231, 222]}

df = pd.DataFrame(data)

sns.lineplot(x=data['Age'], y=data['Weight'])
plt.show()