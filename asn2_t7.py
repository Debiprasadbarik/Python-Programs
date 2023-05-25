list=[2,6,2,7,8,0,1,4,6,7,2,12,9,13,24,12,13,6,9,0]
i=0
even_sum=0
odd_sum=0
odd=0
even=0
while i!=20:
    if list[i]%2==0 and list[i]%4!=0:
        even_sum+=list[i]
        even+=1
    elif list[i]%2!=0 and list[i]%5!=0:
        odd_sum+=list[i]
        odd+=1
    i+=1
print("difference of AVG of even and odd is:",abs(even_sum/even-odd_sum/odd))
