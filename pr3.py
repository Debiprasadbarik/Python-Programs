n=int(input())
num=[None]*n
for i in range(n):
    ele=int(input())
    num[i]=ele
num.sort()
print("3rd lar",num[0])
print("2nd smallest",num[1])