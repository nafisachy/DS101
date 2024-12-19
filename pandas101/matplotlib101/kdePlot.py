import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(200)
y = np.random.randn(200)

# sb.kdeplot(x, shade=True, color="Green", vertical=True)
# sb.kdeplot(y)
sb.kdeplot(x=x,y=y,fill=True, cmap="winter_r", cbar=True)
# plt.show()

iris = pd.read_csv("Iris.csv")
print(iris)

setosa = iris.loc[iris.Species=="setosa"]
virginica = iris.loc[iris.Species == "virginica"]
sb.kdeplot(x=setosa.PetalLengthCm, y=setosa.PetalWidthCm)
sb.kdeplot(x=setosa.SepalWidthCm, y=setosa.SepalLengthCm)
# sb.kdeplot(x=virginica.PetalLengthCm, y=virginica.PetalWidthCm)
plt.show()