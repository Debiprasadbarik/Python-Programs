import math
def factoria(num):
  return(math.factorial(num))
n=int(input())
j=factoria(n)
k=0
for i in range(n):
  k=k+factoria(i)
res=j-k+1
print(res)