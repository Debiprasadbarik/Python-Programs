import math
def factoria(num):
  return(math.factorial(num))
n=int(input())
j=factoria(n)
k=0
for i in range(1,n):
  k=k+factoria(i)
res=j-k
print(res)