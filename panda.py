# write a program to summarise your data set write a program to find invalid missing value and deal with following
# ways fill up with a constant value and constant value is the avg of all the data available in dataset ii- fill up
# the missing value using the data of previous row iii-fill up the missing value using the data of previous next row
# iv-fill up the missing value using the data of previous column v-fill up the missing value using the largest data
# available in the column vi-fill up the missing value using the largest and smallest in that row vii-wrp to find
# available in the dataset in following way 1-row index 2-column index 3-first column 4-4th column in descending
# order 5-1st and 2nd column using merge sorted 6-3rd and 4th column using quicksort 7-2th and 4th column using
# heapsort
import pandas as pd
st = {'roll no': [121, 122, 123], 'name': ['abc', 'def', 'ghi'], 'branch': ['cse', 'me', 'civil'], 'c': [67, 78, 45],}
df = pd.DataFrame(st, index=['s1', 's2', 's3', 's5', 's6'])
df['c'] = df['c'] * 1.5
df['c++'] = [56, 57, 79]
df['java'] = [45, 67, 90]
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
print(df)