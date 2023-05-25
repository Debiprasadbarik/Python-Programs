import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

l = [5, 6, 10, 8, 9, 14]
s = pd.Series(l, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)
print(s['c'])
print(s[['d', 'e', 'f']])
print(s[3])
print(s[-3:])
print(s[:3])
# wrp to create dataframe list tuple dictionary array and series
l = [[121, 'XYZ', 'CSE', 54], [122, 'ABC', 'ME', 55], [123, 'DEF', 'CIVIL', 56]]
df = pd.DataFrame(l, index=['a', 'b', 'c'], columns=['Rollno', 'Name', 'Branch', 'Mark'])
print(df)
# combination of dictionary with list
l = {'rollno': [121, 122, 123],
     'name': ['xyz', 'abc', 'def'],
     'branch': ['cse', 'me', 'civil'],
     'mark': [54, 55, 56]}
df1 = pd.DataFrame(l, index=['a', 'b', 'c'])
print(df1)
# dictionary with numpy
m = {'rollno': np.arange(121, 124),  # we can also use np.array
     'name': ['xyz', 'abc', 'def'],
     'branch': ['cse', 'me', 'civil'],
     'mark': np.arange(54, 57)}
n = pd.DataFrame(m, index=['a', 'b', 'c'])
print(n)
# dictionary with series
m = {'rollno': np.arange(121, 124),  # we can also use np.array
     'name': ['xyz', 'abc', 'def'],
     'branch': ['cse', 'me', 'civil'],
     'mark': pd.Series(21, index=['a', 'b', 'c'])}
n = pd.DataFrame(m, index=['a', 'b', 'c'])
print(n)
# question
l = [{'a': 5, 'b': 6, 'd': 8, 'e': 9}]
# questions

d = {'rollno': pd.Series(np.arange(121, 124), index=['a', 'b', 'c']),
     'name': ['xyz', 'abc', 'def'],
     'branch': ['cse', 'me', 'civil'],
     'mark': pd.Series(21, index=['a', 'b', 'c'])}
n = pd.DataFrame(d, index=['a', 'b', 'c'])
print(n)
d = {'rollno': pd.Series(np.arange(121, 124), index=['a', 'b', 'c']),
     'name': ['xyz', 'abc', 'def'],
     'branch': ['cse', 'me', 'civil'],
     'mark': pd.Series(21, index=['a', 'b', 'c'])}
n = pd.DataFrame(d, index=['a', 'b', 'c'], dtype='S20')
print(n)
a = matplotlib.__version__
print(a)
a = np.arange(1, 10)
b = np.sin(a)
plt.bar(a, b, )
plt.title('sin function')
plt.xlabel('Range')
plt.ylabel('Sin of range')
plt.show()
st = {'roll no': [121, 122, 123], 'name': ['abc', 'def', 'ghi'], 'branch': ['cse', 'me', 'civil'], 'c': [67, 78, 45]}
df = pd.DataFrame(st, index=['s1', 's2', 's3'])
print(df)
print(df['roll no'])
print(df['roll no'][1])
# print(df['roll no', 'name'])
print(df[['roll no', 'c'][1:]])
print(df[['roll no'][1:]])
df['c'][0] = 97
df['c'] = df['c'] * 1.5
df['c++'] = [56, 57, 79]
df['java'] = [45, 67, 90]
df['total'] = df['c'] + df['c++'] + df['java']
print(df)
print(df.loc['s1'])
print(df.iloc[:2])
st1 = {'roll no': [124, 125, 126], 'name': ['jkl', 'mno', 'pqr'], 'branch': ['cse', 'me', 'civil'], 'c': [67, 78, 45]}
df1 = pd.DataFrame(st1, index=['s1', 's2', 's3'])
df1['c'][0] = 97
df1['c'] = df1['c'] * 1.5
df1['c++'] = [56, 57, 79]
df1['java'] = [45, 67, 90]
df1['total'] = df1['c'] + df1['c++'] + df1['java']
df = df.append(df1)
df.insert(1, 'phone', [12, 15, 13, 4, 7, 8])
print(df)
s = pd.Series(np.array([56, 89, 80, 43, 34]))
print(s)
print("Axis:-", s.axes)
print("Datatype", s.dtype)
print("Empty or not", s.empty)
print("no of dimention", s.ndim)
print("no of elements", s.size)
print("original data", s.values)
print("first 2 elements", s.head(2))
print("last 2 elements", s.tail(2))
s = pd.DataFrame(
    {'name': ['A', 'B', 'C', 'D', 'E'], 'Mark': [56, 89, 89, 34, 23], 'weight': [34.7, 67.6, 89.8, 45.3, 67.9]},
    index=['r1', 'r2', 'r3', 'r4', 'r5'])
print(s)
print("summation", s.sum())
print("no of element in each column", s.count())
print("mean of all data", s.mean())
print("value available in middle", s.median())
print("standard deviation", s.std())
print("to give mode value", s.mode())
print("min value in column", s.min())
print("max value in column", s.max())
print(s.describe(include='all'))
print(s)
