'''difference between avg of all even digits except 4 and avg of all odds except 3'''
'''from itertools import count
import math as ma
n=int(input("enter digit no:"))
a=int(input("enter the no:"))
re=0
count=0
count2=0
re2=0
for i in range(n):
    m=a%10
    a=a//10
    if m%2==0 and m!=4:
        d=m
        count+=1
        re=re+d
    elif m%2!=0 and m!=3:
        e=m
        count2+=1
        re2=re2+e
diff=(re//count)-(re2//count2)
print("difference is:",diff)
'''
#sum of product of consecutive no
'''n=int(input("enter no of diugit:"))
a=int(input())
re=0
for i in range(n):
    m=a%10
    a=a//10
    re=re+m*(a%10)
print(re)
'''
#sum of  product of consecutive prime  no
'''def isprime(m):
    count=0
    for i in range(2,m-1):
        if m%i==0:
            count+=1
    if count>=1:
        return 0
    else:
        return 1

n=int(input("enetr no of digits:"))
a=int(input("enter a no:"))
re=0
for i in range(a):
    m=a%10
    a=a//10
    if isprime(m)==1:
        mi=m
        re=re*10+mi
res=0
while re:
    remain=re%10
    re=re//10
    res=res+remain*(re%10)
print(res)
'''
#1-x2/2!+x3/3!+x4/4!+...
'''def fact(y):
    fac=1
    for j in range(2,y+1):
        fac*=j
    return fac


x=int(input("enter value for x:"))
n=int(input("enter value for n:"))
res=0
for i in range(2,n+1):
   re=(x**i)/fact(i)
   res=res+re
result=1-res
print(result)
'''
#list of prime no as per given range
'''def prime(y):
    count=0
    for i in range(2,y//2):
        if y%i==0:
            count=1
    if count>=1:
        return 0
    else:
        return 1

a=int(input("enter starting range:"))
b=int(input("enter end range:"))
lis=[]
for i in range(a,b):
    if prime(i)==1:
        lis.append(i)
print(lis)
'''
#dictionary
'''dict={0:'math',1:'sci',2:'eng',3:'c',4:'java'}
d={}
sub=0
tm,std=0,0
while sub!=5:
    tm=tm+int(input("enter your {} marks:".format(dict[sub])))
    sub+=1
print("your total mark:",tm)
tm=0
sub+=1    
'''
'''lis=[]
for i in range(10):
    s=input("enter fruits name:")
    lis.append(s)
print(lis)'''
#no of occurance
'''lis=[]
n=int(input("enter no:"))
for i in range(n):
    a=int(input("enter:"))
    lis.append(a)
print(lis)
lis.sort()
print(lis)
count=0

for j in range(n-1):
    if lis[j]==lis[j+1]:
        count+=1
        k=lis[j]
        print(k,count)
'''
#prime fibonacci series

def prime(y):
    count=0
    if y==1:
        return 0
    else:
        for i in range(2,y//2):
            if y%i==0:
                count=1
        if count>=1:
            return 0
        else:
            return 1
def fibbo(w,z):
    a,b,c=0,1,1
    result=0
    while a<=z:
        if a>=w:
            result+=1
            a=b
            b=c
            c=a+b

    return a
f=int(input("enter 1st range:"))
l=int(input("enter 2nd range:"))
final=fibbo(f,l)
if prime(final)==1:
    print(final)