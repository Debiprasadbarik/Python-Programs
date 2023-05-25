a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
product_sum=0
while a:
    product_sum+=a%10*(b%10)
    a//=10
    b//=10
print("sum of product of two corressponding digits:",product_sum)