a=int(input("enter your range:"))
b=int(input("enter:"))
j=0
list=[]
while a!=b:
    allow=1
    for i in range(2,a//2):
        if a%i==0:
            allow=0
            break
    if allow:
        list.insert(j,a)
        j+=1
    a+=1
print(list)