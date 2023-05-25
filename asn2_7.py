n=int(input("enter no of digit"))
p_sum=0
num=int(input("enter the no:"))
for i in range(n):
    m=num%10
    num=num//10
    p_sum=p_sum+m*(num%10)
print("sum of product of consecutive :",p_sum)