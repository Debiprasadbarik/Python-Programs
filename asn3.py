num=int(input("enter a 4 digit no:\n"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
num=num//10
d=num//1
e=1000*a+100*b+10*c+1*d
print("reversed no is:",e)