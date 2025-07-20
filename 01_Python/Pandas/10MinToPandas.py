# 10 minutes to Pandas 

# We import pandas 
import numpy as np
import pandas as pd 

# Basic Data Structure in Pandas 
# 1. Series: a one-dimensional labeled array holding data of any type
# 2. DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a tbale with rows and columns.

# Object creation

# Creating a Series by passing a list of values, letting pandas create a default RangeIndex.

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

# Creating a DataFrame by passing a NumPy array with a datetime index using date_range() and labeled columns:

dates = pd.date_range("20250101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=list("ABCDE"))

print(df)


