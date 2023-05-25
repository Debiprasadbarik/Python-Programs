list=[2,6,2,7,8,0,1,4,6,7,2,12,9,13,24,12,13,6,9,0]
i=0
count=1
list.sort()
while i!=19:
    if list[i]==list[i+1]:
        count+=1
    else:
        print(" occurs for times",(list[i],count))
        count=1
    i+=1
print(" occurs for times",(list[i],count))
