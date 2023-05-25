n=int(input("enter the no of digits:"))
num=int(input("enter digit:"))
k=int(input("enter the kth value:"))
forward=((num//(10**(n-k)))%10)
backward=((num//(10**(k-1)))%10)
pf=(10**(n-k))*forward
pb=(10**(k-1))*backward
print("counting the starting position as 1....")
print("from forward",k,"th value:",forward)
print("from backward",k,"th value:",backward)
print("from forward",k,"th position value:",pf)
print("from backward",k,"th position value:",pb)