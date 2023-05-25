a=int(input("enter your number:"))
sum_even=0; sum_odd=0;
i=0; j=0; prod=0; prod1=0; 
while a:
    if (a%10)%2==0 and a%10!=2 and a%10!=6:
        prod=(a%10)*j
        j=a%10
        sum_even+=prod
    elif (a%10)%2!=0 and a%10!=3 and a%10!=7:
        prod1=(a%10)*i
        i=a%10
        sum_odd+=prod1
    a//=10
print("difference is:",sum_even-sum_odd)
