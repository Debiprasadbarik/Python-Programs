list=[2,6,5,8,12,4,0,12,45,78,90,34,56,1,3,99,43,65,67,68]
list.sort()
i=0
large=0
small=0
while i!=3:
    print("{}th largest number is:{}".format(i+1,max(list)))
    list.remove(max(list))
    print("{}th smallest number is:{}".format(i+1,min(list)))
    list.remove(min(list))
    i+=1
