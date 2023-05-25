num=int(input("enter a 4 digit no:\n")) #1122
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
num=num//10
d=num//1
sum=a+b+c+d
print("submmation of all 4 digit is:",sum)