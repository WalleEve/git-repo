import pandas as pd
import numpy as np

data = [1, 2, 3, 4]
s = pd.Series(data)
print(s)


data = [1, 2, 3 , 4]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)


"""
data = [1, 2, 3, 4]
s = pd.Series(data, index=['a', 'b', 'c']) # ValueError: Length of passed values is 4, index implies 3.
print(s)
"""

data = [1, 2, 3, 4]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s['a'])
print(s[:3])
print(s[:-1])

s = s.drop('d')
print(s)

data1 = [5, 6, 7]
s2 = pd.Series(data1)

s = s.append(s2)
print(s)


data3 = [10, 11, 13]

s3 = pd.Series(data3)

s = s + s3
print(s)


data1 = [1, 2, 3, 4]
data2 = [1, 2, 3, 4]

data1Seriea = pd.Series(data1)
data2Series = pd.Series(data2)

data1Seriea = data1Seriea + data2Series
# AXIS
s = pd.Series(np.random.randn(4))
print("Original Series value:")
print(s)
print("axes of Series")
print(s.axes)

# NDIM
s = pd.Series(np.random.randn(4))
print("Original Series Value")
print(s)
print("Series NDIM Value")
print(s.ndim)

# EMPTY
s = pd.Series(np.random.randn(5))
print("Origina Series Value:")
print(s)
print("Series is Empyty or Not")
print(s.empty)

# SIZE

s = pd.Series(np.random.randn(5))
print("Original Series Value:")
print(s)
print("Size of Series:")
print(s.size)

# HEAD()

s = pd.Series(np.random.rand(5))
print("Original Series Value:")
print(s)
print("Top 2 Element")
print(s.head(2))

# TAIL()
import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5))
print("Original Series Value:")
print(s)
print("Last 2 Element")
print(s.tail(2))
print(f" Values: {s}")
