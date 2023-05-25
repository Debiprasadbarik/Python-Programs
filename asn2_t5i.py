a=input("enter your string:")
i=0
if len(a)<3:
    print(a)
else:
    str_len=len(a)
    if a[str_len-1]=='g' and a[str_len-2]=='n' and a[str_len-3]=='i':
        b=" "
        for i in range(str_len-3):
            b+=a[i]
        l="ly"
        b+=l;
        print("string is:{}".format(b))
    else:
        b="ing"
        a+=b
        print(a)
