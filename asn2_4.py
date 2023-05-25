import math
print("enter the total digit no:")
n=int(input())
num=int(input())
sum1=0
for i in range(n):
      m=num%10
      num=num//10
      if m%2!=0:
          r=m
          sum1=sum1+r
print("sum of all odd digits is:",sum1)