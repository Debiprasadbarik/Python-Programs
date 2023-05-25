n=int(input("enter the no of digits:"))
num=int(input("enter the no:"))
count1,count2=0,0
sum1,sum2=0,0
for i in range(n):
    m=num%10
    num=num//10
    if (m%2==0 and m%4!=0):
        count1=count1+1
        r=m
        sum1=sum1+r
    elif (m%2!=0 and m%3!=0):
        count2=count2+1
        s=m
        sum2=sum2+s

avg1=sum1//count1
avg2=sum2//count2
print("difference is:",avg1-avg2)