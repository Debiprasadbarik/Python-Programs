num=int(input("enter a 4 digit no:\n"))
k=int(input("enter the position no:\n"))
n=((num//(10**(4-k)))%10)
print("digit at position",k,"is",n)