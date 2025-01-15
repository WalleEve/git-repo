import pandas as pd 
import numpy as np 


df = pd.DataFrame(np.random.randn(5), columns = ["Random_Value1"])
print(df)


df = pd.DataFrame([["A", "B"], ["C", "D"]], columns = ["Alpha1", "Alpha2"])
print(df)


df = pd.DataFrame([[1, 2], [4, 5]],  columns=["A", "B"])
print(df) 

df = pd.DataFrame([1, 2, 3, 4, 5], columns = ["A"])
print(df)

d = {"Name":pd.Series(["Tom", "Hanes", "Jack", "Jill", "Steve"]),
"Age":pd.Series([23, 34, 25, 26, ]),
"Rating":pd.Series([3.4, 2.9, 4.3, 3.9, 4.7])}

df = pd.DataFrame(d)
print(df) 


# TRANSPOSE:
d = {
    "Name":pd.Series(["Tom", "James", "Jack", "Jill", "Steve", "Yen"]),
    "Age":pd.Series([23, 45, 26, 20, 19, 29]),
    "Rating":pd.Series([4.12, 3.4, 4.5, 3.9, 2.8, 3.7])
}

df = pd.DataFrame(d)
print("Transpose of the Data Series: ")
print(df.T)


# AXES 
d = {
    "Name":pd.Series(["James", "Tom", "Smith", "Steve"]),
    "Age":pd.Series([23, 45, 26, 34]),
    "Rating":pd.Series([4.3, 2.5, 3.4, 3.9])
}

df = pd.DataFrame(d)
print("Original Data Frame")
print(df) 

print("row axis label column axis label")
print(df.axes) 

# DTYPES : Data type for each column 

d = {
    "Name": pd.Series(["Steve", "James", "Smith", "Scott"]),
    "age": pd.Series([23, 35, 25, 45]),
    "dob": pd.Series(["2 APR 1991", "3 MAR 1992", "4 FEB 1990", "19 AUG 1984"]),
    "rating": pd.Series([3.5, 4.5, 2.9, 3.7])
}

df = pd.DataFrame(d)
print(df) 
print("Data Type of each column: ")
print(df.dtypes) 


# EMPTY 

d = {
    "Name": pd.Series(["Smith", "Steve","Scott"]),
    "Age": pd.Series([23, 29, 38]),
    "Rating": pd.Series([3.4, 4.8, 3.9])
}

df = pd.DataFrame(d)
print("Check if the Frame is empty")
print(df.empty)
print("Original Data Frame ")
print(df)


df = pd.DataFrame()
print("Check if the Data Frame is empty")
print(df.empty)
 
# NDIM: 
d = {
     "Name": pd.Series(["Scott", "Smith", "Steve", "John"]),
     "Age": pd.Series([24, 35, 45, 34]),
     "Rating": pd.Series([2.4, 3.4, 3.9, 4.9])
}

df = pd.DataFrame(d)
print("Original Data Frame ")
print(df)

print("Dimention of Object:")
print(df.ndim)

# SHAPE 


d = {
     "Name": pd.Series(["Scott", "Smith", "Steve", "John"]),
     "Age": pd.Series([24, 35, 45, 34]),
     "Rating": pd.Series([2.4, 3.4, 3.9, 4.9])
}

df = pd.DataFrame(d)
print("Original Data Frame ")
print(df)

print("Share of Object:")
print(df.shape) # Returns number of rows and columns 


# SIZE 
d = {
     "Name": pd.Series(["Scott", "Smith", "Steve", "John"]),
     "Age": pd.Series([24, 35, 45, 34]),
     "Rating": pd.Series([2.4, 3.4, 3.9, 4.9])
}

df = pd.DataFrame(d)
print("Original Data Frame ")
print(df)

print("Size of Object:")
print(df.size) # Return total number of records

# VALUES:
d = {
     "Name": pd.Series(["Scott", "Smith", "Steve", "John"]),
     "Age": pd.Series([24, 35, 45, 34]),
     "Rating": pd.Series([2.4, 3.4, 3.9, 4.9])
}

df = pd.DataFrame(d)
print("Original Data Frame ")
print(df)

print("Values of Object:")
print(df.values)  # Return Original value of an DataFrame object 

# HEAD() / TAIL() 
d = {
     "Name": pd.Series(["Scott", "Smith", "Steve", "John", "Ele", "Mike", "Denver"]),
     "Age": pd.Series([24, 35, 45, 34, 35, 36, 34]),
     "Rating": pd.Series([2.4, 3.4, 3.9, 4.9, 3.5, 4.5, 3.9])
}

df = pd.DataFrame(d)
print("Original Data Frame ")
print(df)

print("First two records from the DataFrame Object:")
print(df.head(2)) # Returns First two records .
print("Returns Default top five records ")
print(df.head()) # Return first 5 values default

print("Last two records fromthe DataFrame Object")
print(df.tail(2)) # Returns Last two Recods of an Object
print("Returns Default bottom 5 records")
print(df.tail()) # Return last Five Records on an Object Default
