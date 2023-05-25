def isprime(n):
    count=0
    for i in range(2,n//2):
        if n%i==0:
            count+=1
    if count>=1:
        return 0
    else:
        return 1
flag=0
no=int(input("enter no:"))
for i in range(2,1000000):
    if isprime(i)==1:
        flag+=1
        #print(flag,":prime no=",i)     #104729
        if flag==no:
            print(i)