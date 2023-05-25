import math
print("enter the total digit no:")
n=int(input())
num=int(input())
sum2=0
for i in range(n):
      m=num%10
      num=num//10
      if m==2 or m==3 or m==5 or m==7:
            r=m
            sum2=sum2+r
print("sum of all prime digits is:",sum2)