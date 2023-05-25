#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
def palin(n):
    k=0
    p=n
    while n>0 :
        m=n%10
        k=(k*10)+m
        n=n//10
    if k==p:
        return 1
    else:
        return 0
n=999
larpar=101
for i in range(100,n):
    k=i*(i+1)
    if palin(k)==1:
        if k>larpar:
            print(k)
    
