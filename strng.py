#program to give output a string after replacing the indexed char to last index
s=input("enter a string:") #debiprasad
n=int(input("enter the index no:")) #3
l=len(s) #10
d=s[n] +s[0:n]+s[n+1:]
print(d)