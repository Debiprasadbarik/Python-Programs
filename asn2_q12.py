n=int(input())
m=int(input())
sum=0
while n>0 and m>0:
    sum=sum+(n%10)*(m%10)
    n=n//10
    m=m//10
print(sum)