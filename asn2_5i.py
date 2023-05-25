num=int(input("enter your value:"))
x=0;n=0
while num:
    if (num%10)%2==0 and num%10!=2 and num%10!=8:
        x+=num%10
    elif (num%10)%2!=0 and num%10!=3 and num%10!=1:
        n+=num%10
    num//=10
print("value of x is:", "and value of n is:",x,n)
