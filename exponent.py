def check(a,b):
    res=1
    for i in range(1,b+1):
        res=res*a
    return res
no=int(input())
ok=no
resu=[]
while ok>0:
    n1,n2=[int(x) for x in input().split()]
    ele=check(n1,n2)%1000000007
    resu.append(ele)
    ok-=1
for j in range(no):
    print(resu[j])

