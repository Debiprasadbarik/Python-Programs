n=int(input("enter ano:"))
count1=0
count2=0
sum1,sum2=0,0
while n>0:
    rem=n%10
    n=n//10
    if rem%2==0 and rem!=4:
        count1+=1
        sum1=sum1+rem
    elif rem%2!=0 and rem!=3:
        count2+=1
        sum2=sum2+rem
avg1=sum1/count1
avg2=sum2/count2
diff=avg1-avg2
print(avg1," ",avg2," ",diff)    