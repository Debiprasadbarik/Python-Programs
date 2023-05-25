i=0
a=" "
while i!=3:
    a+=input("enter your fruits name:")
    a+=" "
    i+=1
#storing the value of string into a list to sort
list=[word.lower() for word in a.split()]
list.sort()
print(list)
