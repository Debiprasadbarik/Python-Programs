a=int(input("enter your number:"))
product_sum=0
b=0
while a:
    if (a%10)%2==0:
        product_sum+=b*(a%10)
        b=a%10
    a//=10
    
print("product of all consecutive even digits of given number is:",product_sum)
