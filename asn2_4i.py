x=int(input("enter your number:"))
n=int(input("enter the value of n:"))
sum=1
for i in range(2,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j

    pow=(x**i)/fact

    if i%2==0:
        pow=-pow

    sum+=pow
print("sum of the series is:",sum)
