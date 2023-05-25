# n=int(input())
# m=int(input())
# sum=0
# while n>0 and m>0:
#     m1=n%10
#     m2=m%10
#     if m1%2==0 and m2%2!=0:
#         sum=sum+(m1)*(m2)
#     n=n//10
#     m=m//10
# print(sum)

# import math
# x=int(input())
# n=int(input())
# sum=0
# for i in range(3,n+1,2):
#     y=(x**i)/math.factorial(i)
#     if i%2==0:
#         sum=sum-y
#     else:
#         sum+=y
# print(x-sum)

# import sympy;x=int(input());y=int(input());print(list(sympy.primerange(x,y)))
# import sympy;
# x=int(input());y=int(input());
# lis=[]
# for i in range(x,y+1):
#     if sympy.isprime(i):
#         lis.append(i)
# print(lis)

# thisdict={
# 0:"maths",
# 1:"english",
# 2:"dbms",
# 3:"python",
# 4:"java"
# }
# num_stu=0
# while num_stu!=10:
#     num_sub=0; total_marks=0
#     print("enter your five subject marks:")
#     while num_sub!=5:
#         total_marks+=int(input("enter your" + thisdict[num_sub] +" marks:"))
#         num_sub+=1
#     print("your total marks is:",total_marks)
# total_marks=0; 
# num_stu+=1

# n=int(input())
# lis=[0,1]
# for i in range(2,n):
#     x = lis[i-2]+lis[i-1]
#     lis.append(x)

# print(lis)
# a=input("enter your string:")
# i=0
# if len(a)<3:
#    print(a)
# else:
#     str_len=len(a)
#     if a.endswith("ing"):
#         b=" "
#         b=a+"ly"
#         print("string is:",b)
#     else:
#         b="ing"
#         a+=b
#         print(a)
# c="$"
# d=c+a[1:]
# print(d)

# i=0
# a=" "
# while i<3:
#     a+=input("enter:")+" "
#     i+=1
#     lis=[]
#     lis=a.split()
#     lis.sort()
# print(lis)

# l=(22/7,2.68)
# area=l[0]*(l[1]**2);print(area)

# def prime(x):
#     count=0
#     if x<=1:
#         return 0
#     for i in range(2,x-1):
#         if x%i!=0:
#             count+=1
#     if count>=1:
#         return 1
#     else:
#         return 0

# x=int(input("1st range:"))
# y=int(input("2nd range:"))
# lis=[0,1]
# for i in range(2,y):
#     a=lis[i-2]+lis[i-1]
#     # if prime(x) 
#     lis.append(a)
# print(lis)
# print(prime(7))

# s=[]
# for i in range(y):
    
#     if (lis[i]>=x and lis[i]<= y):
#          if prime(lis[i]):
#             s.append(lis[i])
# print(s)

# bal=5000
# amt=int(input("enter amount:"))
# s=0
# try:
#     if amt<bal:
#         bal=bal-amt
#         s=1
#     else:
#         raise ValueError(amt)
# except ValueError as e:
#     print("failed",e.args[0])
#     s=0
# else:
#     print("you can withdraw",amt)
#     s=1
# finally:
#     if s==0:
#         print("failed")
#     else:
#         print("done")

# import numpy as np 
# a = np.array([[1, 2,3],[ 3,4,5]], ndmin = 2)
# print (a)
import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.reshape(2,3,1))
a.shape = (3,2)
print(a)
