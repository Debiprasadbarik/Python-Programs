import math
print("enter the total digit no:")
n=int(input())
num=int(input())
sum2=0
for i in range(n):
      m=num%10
      num=num//10
      for j in range(2,m-1):
          if m%j!=0:
              r=m
              sum2=sum2+r
print("sum of all prime digits is:",sum2)