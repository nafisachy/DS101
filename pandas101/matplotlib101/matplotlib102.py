import matplotlib.pyplot as plt
import pandas as pd

# Pyplot line chart
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()


df = pd.read_csv("../Iris.csv")

# Bar chart
# Plot a simple bar chart
plt.bar(df['Species'], df['SepalLengthCm'])

# Title the plot
plt.title("Iris Dataset")

# Adding legends
plt.legend(["bar"])
plt.show()


# Histogram chart
plt.hist(df["SepalLengthCm"])
plt.title("Histogram")
plt.legend(["SepalLengthCm"])
plt.show()


# Scatter plot
plt.scatter(df["Species"], df["SepalLengthCm"])
plt.title("Scatter Plot")
plt.legend(["SepalLengthCm"])
plt.show()


# Box Plot
plt.boxplot(df["SepalWidthCm"])
plt.title("Box Plot")
plt.legend(["SepalWidthCm"])
plt.show()


# Correlations Heatmap
plt.imshow(df.corr(), cmap="autumn", interpolation="nearest")
plt.title("Heat Map")
plt.show()