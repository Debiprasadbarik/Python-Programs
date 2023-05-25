#write a program to find difference between the largest and the smallest element amng 3 nos
n=int(input())
num=[None]*n
for i in range(n):
    ele=int(input())
    num[i]=ele
m=max(num)
m1=min(num)
r=m-m1
print("difference between largest and smallest is:",r)