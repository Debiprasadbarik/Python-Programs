n=int(input())
i=2
flag=0
for i in range(1,n-1):
    if n%i==0:
        flag=flag+1
if(flag>0):
             print("not prime")
else:
            print("prime")