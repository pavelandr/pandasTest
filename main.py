import pandas as pd
import numpy as np

# Series

x = ['a', 'b', 'c', 'd', 'e']
x2 = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]
z = {1: 'a', 2: 'b', 3: 'c'}

print(pd.Series(x))  # Serialize x by indexing from 0

print(pd.Series(y, x))  # Serialize y by using x as the indexer

print(pd.Series(z))  # Serialize dictionary

a = pd.Series(y, x)  # Arithmetics on series
b = pd.Series(y, x2)
print(a + b)

print(a['a'])  # Access value in series by indexer value.
print(a['c':'e'])  # Series slicing

##############
# DataFrames

A = [1, 2, 3, 4]
B = [2, 3, 4, 5]
C = [2, 3, 2, 4]
D = [7, 8, 9, 0]
E = [1, 3, 5, 2]

df = pd.DataFrame([A, B, C, D, E], ['a', 'b', 'c', 'd', 'e'],
                  ['W', 'X', 'Y', 'Z'])  # Define dataframe (rows then columns)
print(df)

df['P'] = df['Y'] + df['Z']  # Add column
print(df)

print(df.drop('e'))  # Delete row in the instance.
print(df)

df.drop('e', inplace=True)  # Delete row permanently
print(df)

df.drop('P', axis=1, inplace=True)  # Delete column
print(df)

print(df['Y'])  # Accessing column

print(df.loc['a'])  # Accessing row
print(df.iloc[0])  # Accessing row by index

print(df.loc['b', 'W'])  # Accessing element

print(df > 3)  # Conditional selection
print(df[df > 3])  # Conditional selection
print(df[df['W'] > 1])  # Conditional selection in coloumn - all the rows that stisfy the condition
print(df[df['W'] > 1][['W', 'X']])  # Conditional selection in coloumn -
# all the rows that stisfy the condition and selecting columns from them
print(df[df['W'] > 1]['W'])  # Conditional selection in coloumn -
# all the rows that stisfy the condition and selecting columns from them
print(df[(df['W'] > 4) & (df['W'] > 4)])  # Conditional selection in coloumn - multiple conditions
print(df[(df['W'] > 4) | (df['W'] > 4)])  # Conditional selection in coloumn - multiple conditions

##############
# Missing Data
##############

d = {'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, np.nan], 'c': [0, 1, 2, np.nan, np.nan],
     'd': [3, 4, np.nan, np.nan, np.nan], 'e': [5, np.nan, np.nan, np.nan, np.nan]}
d1 = pd.DataFrame(d)
print(d1)
print(d1.dropna(axis=0))  # drop all rows with NaN values
print(d1.dropna(axis=1))  # drop all columns with NaN values
print(d1.dropna(thresh=3))  # drop all rows that have less than 3 availible elements.
print(d1.fillna(1))  # replace all NaN value in 1
print(d1['b'].fillna(value=d1['b'].mean()))  # replace NaN value in column 'b' with average of the column

##############
# GroupBy
##############

p = {'item': ['apple', 'apple', 'orange', 'orange', 'guns', 'guns', 'guns'],
     'days': ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'],
     'sales': [100, 80, 200, 100, 5, 10, 5]}
df = pd.DataFrame(p)
x = df.groupby('item')  # Group by item
print(x.mean())  # Find mean
print(x.sum())  # Sum
print(x.std())  # Standart Diviation
print(x.count())  # Count
print(x.max())  # Find maximal values
print(x.describe())  # Print Mean,Std,min,25%,50%,75%, max
print(x.describe().transpose())  # Transpose the table

##############
# Joining
##############

x1 = {'a': [1, 2, 3], 'b': [5, 6, 7]}
y1 = {'c': [3, 4, 5], 'd': [2, 3, 6]}

x = pd.DataFrame(x1, index=['p1', 'p2', 'p3'])
y = pd.DataFrame(y1, index=['p1', 'p2', 'p3'])
print(x)
print(y)

print(x.join(y))  # Join x and y to one data frame

x = pd.DataFrame(x1, index=['p1', 'p2', 'p3'])
y = pd.DataFrame(y1, index=['p1', 'p4', 'p5'])
print(f"LEFT\n{x.join(y, how='left')}")  # Join x and y with diffrent index numbers
print(f"RIGHT\n{x.join(y, how='right')}")
print(f"INNER\n{x.join(y, how='inner')}")
print(f"OUTER\n{x.join(y, how='outer')}")

##############
# Concatinating
##############
x1 = {'a': [1, 1, 1, 1, 1], 'b': [1, 1, 1, 1, 1], 'c': [1, 1, 1, 1, 1], 'd': [1, 1, 1, 1, 1], 'e': [1, 1, 1, 1, 1]}
x2 = {'e': [2, 2, 2, 2, 2], 'f': [2, 2, 2, 2, 2], 'g': [2, 2, 2, 2, 2], 'h': [2, 2, 2, 2, 2], 'i': [2, 2, 2, 2, 2]}
x3 = {'a': [3, 3, 3, 3, 3], 'b': [3, 3, 3, 3, 3], 'c': [3, 3, 3, 3, 3], 'd': [3, 3, 3, 3, 3], 'e': [3, 3, 3, 3, 3]}

df1 = pd.DataFrame(x1, index=[1, 2, 3, 4, 5])
df2 = pd.DataFrame(x2, index=[1, 2, 3, 4, 5])
df3 = pd.DataFrame(x3, index=[5, 6, 7, 8, 9])

print(pd.concat([df1, df2]))  # Concatination of df1 and df2 by columns
print(pd.concat([df1, df2], axis=1))  # Concatination of df1 and df2 by rows

##############
# Merging
##############
df1 = pd.DataFrame({'key1': [1, 2, 3], 'a': [2, 3, 4], 'b': [5, 6, 7]})
df2 = pd.DataFrame({'c': [1, 2, 9], 'd': [5, 8, 9], 'key1': [1, 2, 3]})
print(pd.merge(df1, df2, on='key1'))  # Merging using key1 as an index

df1 = pd.DataFrame({'key1': [1, 2, 3], 'a': [2, 3, 4], 'b': [5, 6, 7]})
df2 = pd.DataFrame({'c': [1, 2, 9], 'd': [5, 8, 9], 'key1': [1, 2, 4]})

print(pd.merge(df1, df2, how='inner', on='key1'))  # the key values of the dateframe are different,and if we use
# how=inner then the different values won't be shown
print(pd.merge(df1, df2, how='outer', on='key1'))  # On the other hand using how=outer they will be shown as NaN
print(pd.merge(df1, df2, how='left', on='key1'))  # On the other hand using how=left only the different
# values of the leftkey be showen
print(pd.merge(df1, df2, how='right', on='key1'))  # Same thing about the how='right'

df1 = pd.DataFrame({'key1': [1, 2, 3], 'a': [2, 3, 4], 'b': [5, 6, 7], 'key2':[5,2,4]})
df2 = pd.DataFrame({'c': [1, 2, 9], 'd': [5, 8, 9], 'key1': [1, 2, 4], 'key2':[5,2,3]})
print(pd.merge(df1, df2, how='outer', on=['key1','key2']))  # Merging by 2 keys

##############
# Operations
##############

x = pd.DataFrame({'a':[1,2,3,4,5], 'b':[20,60,70,40,40]})
print(x)
print(x.columns) # Show dataframe columns

def inc(x):
    return x+100

print(x['b'].apply(inc)) # Apply function on 'b' colomn
print(x.sort_values('b')) # sort dataframe according to 'b' column values
print(x['b'].unique())  # get the unique list of values of column 'b'
print(x['b'].nunique())  # get number of values of column 'b'
print(x['b'].value_counts()) # get a count of every value inside a column