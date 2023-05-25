def prime(a):
    if a<1:
        return 0
    for i in range(2,a//2):
        if a%i==0:
            return 0
        else:
            return 1
def fibo(a,b):
    c=1;i=0
    while i<b:
        if i>a:
            if prime(i):
                print(i)
        i+=c
        c=i-c
        print(c)
a=int(input("enter 1:"))
b=int(input("enter 2:"))
fibo(a,b)
