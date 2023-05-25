#assignment 1 1st qus
'''
n=int(input("how many digit:"))
a=int(input("enter a no:"))
sum=0
for i in range(n):
    reminder=a%10
    sum=sum+reminder
    a=a//10
print("sum of the digit:",sum)
'''
#sum of prime digits
'''n=int(input("how many digits:"))
a=int(input("entera no:"))
sum=0
for i in range(n):
    reminder=a%10
    if reminder==2 or reminder==3 or reminder==5 or reminder==7:
        sum=sum+reminder
    a=a//10
print("sum of prime no:",sum)
'''