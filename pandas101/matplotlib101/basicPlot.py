import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# line chart
# plt.plot(x, y)
# plt.title('Line Chart')
# plt.ylabel('Y-Axis')
# plt.xlabel('X-Axis')
# # plt.show()
#
#
# # bar chart
data = pd.read_csv('tips.csv')
# x = data['day']
# y = data['total_bill']
#
# plt.bar(x, y)
# plt.title('Tips Dataset')
# plt.ylabel('Total Bill')
# plt.xlabel('Day')
# # plt.show()
#
# # histogram
# data1 = pd.read_csv('tips.csv')
# x = data1['total_bill']
#
# plt.hist(x)
# plt.title('Tips Dataset')
# plt.ylabel('Frequency')
# plt.xlabel('Total Bill')
# # plt.show()
#
# # scatter plot
# data2 = pd.read_csv('tips.csv')
# x = data2['day']
# y = data2['total_bill']
#
# plt.scatter(x, y)
# plt.title('Tips Dataset')
# plt.ylabel('Total Bill')
# plt.xlabel('Day')
# plt.show()

# pie chart
# data = pd.read_csv('tips.csv')
#
# cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
# data = [23, 10, 35, 15, 12]
#
# plt.pie(data, labels=cars)
# plt.title('Car data')
# plt.show()

# box plot
# np.random.seed(10)
# data = [np.random.normal(0, std, 100) for std in range(1, 4)]
#
# plt.boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor='skyblue'), medianprops=dict(color='red'))
# plt.xlabel('Data Set')
# plt.ylabel('Values')
# plt.title('Example of Box Plot')
# plt.show()


# heatmap
np.random.seed(0)
data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Example of Heatmap')
plt.show()