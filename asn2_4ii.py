x=int(input("enter your number:"))
n=int(input("enter the value of n(only odd):"))
sum=x
count=0
for i in range(3,2*n-1,2):
    fact=1
    for j in range(1,i+1):
        fact*=j

    pow=(x**i)/fact

    if count%2==0:
        pow=-pow
    count+=1
    sum+=pow
print("sum of the series is:{}".format(sum))
