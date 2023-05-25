alertlimit=10
a=15
i=1
while(i<=a):
    if i>alertlimit:
        print("alert limit crossed")
        break
    print("alert")
    i=i+1
    print(i)
print("i came out of loop")