print("enter the total digit no:")
n=int(input())
num=int(input())
sum=0
for i in range(n):
    m=num%10
    num=num//10
    sum=sum+m
print("sum of all",n,"digits is:",sum)