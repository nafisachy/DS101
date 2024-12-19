import pandas as pd
import numpy as np

# Creating empty series
ser = pd.Series()  # The object is just a column

print(ser)

# Simple array
data = np.array(['g', 'e', 'e', 'k', 's'])  # Creating the array with numpy
ser = pd.Series(data)  # Put the new array in the empty series

print(ser)