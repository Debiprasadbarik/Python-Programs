Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=3
if(a>b):
    print("a is larger")
    else:
        
SyntaxError: invalid syntax
if(a>b):
    print("abjd")
else:
    print("jdi")

    
abjd
10<20<30<40<58
True
23>344>44
False
34>45<456>32
False
10==35
False
10==10
True
0==0
True
1==1
True
1==0
False
0==1
False
10!=20
True
10!=10
False
"debi"=="debi"
True
"debi"=="papa"
False
10==20==34==45
False
10!=23!=24
True
x=12
y=20
x and y
20
x or y
12
y and x
12
y or x
20
True and False
False
True or False
True
if(12==12 or 13==14):
    print("shui")
else:
    print("jidj")

    
shui
if(12==12 | 23==24)
SyntaxError: expected ':'
if(23==23 | 12==13):
    print("jsj")
else:
    print("jij")

    
jij
10==10 |12==23
False
10>12 ^ 12>10
False
12~13
SyntaxError: invalid syntax. Perhaps you forgot a comma?
12~13,
SyntaxError: invalid syntax. Perhaps you forgot a comma?
~12
-13
~-12
11
12~13:
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
~-13
12
bin(-13)
'-0b1101'
#-n-1 for finding compliment of any positive no
int(0b101000)
40
10>>2
2
10<<2
40
a="DELL"
len(a)
4
if(len=4):
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if(len==4):
    print("hello")
else:
    print("no")

    
no
a="DELL"
a[::-1]
'LLED'
if(len(a)==4):
    print("hello")

    
hello
if(len(a)=4):
    
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
1^2
3
2^28
30
23^23
0
23^34
53
45^2
47
x=10
x+=
SyntaxError: invalid syntax
x+=10
print(x)
20
a,b
('DELL', 3)
a,b=10,20
x=30
if a>b else 40
SyntaxError: invalid syntax
x=30 if a<b else 40
print(x)
30
a=int(input("enter 1st no"))
enter 1st no10
b=int(input("enter 2nd no:"))
enter 2nd no:20
min=a if a<b else b
print("minimum value: ",min)
minimum value:  10
a=10
b=20
a is b
False
b is a
False
a="DBI"
b="DBI"
id(a)
2416850626352
id(a) is id(b)
False
a,b=20
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a,b=20
TypeError: cannot unpack non-iterable int object
