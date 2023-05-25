Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
complex(10)
(10+0j)
complex(True)
(1+0j)
complex(False)
0j
complex("10")
(10+0j)
complex("True")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    complex("True")
ValueError: complex() arg is a malformed string
complex("10.5")
(10.5+0j)
complex(10)
(10+0j)
comlex(10.5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    comlex(10.5)
NameError: name 'comlex' is not defined. Did you mean: 'complex'?
complex(10.5)
(10.5+0j)
complex(3,4)
(3+4j)
complex("3,4")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    complex("3,4")
ValueError: complex() arg is a malformed string
complex(True,False)
(1+0j)
complex(10,--2)
(10+2j)
complex(10,-34)
(10-34j)
cc=100
complex(cc)
(100+0j)
bool(True)
True
bool(0)
False
bool(1)
True
bool(5)
True
bool(-2)
True
bool("0")
True
int(10.55555555)
10
int("10.7777")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int("10.7777")
ValueError: invalid literal for int() with base 10: '10.7777'
int("10.5")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int("10.5")
ValueError: invalid literal for int() with base 10: '10.5'
float("10.5")
10.5
bool()
False
int()
0
float()
0.0
complex(0)
0j
bool(none)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    bool(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
bool(None)
False
str(10)
'10'
str(10+78j)
'(10+78j)'
str(10.55)
'10.55'
x=input("enter value)
        
SyntaxError: unterminated string literal (detected at line 1)
x=input(enter value)
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x=input("enter value)
        
SyntaxError: unterminated string literal (detected at line 1)
x=input(10)
        
10x=input("enter value:")
x=input("enter value: ")
        
enter value: 10
print(x)
        
10
print(input)
        
<built-in function input>
x=input(enter value)
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
x=input("enter value")
        
enter value20
x=input("enter value")
        
enter value23
y=input("enter 2nd :")
        
enter 2nd :23
print("sum: ",x+y)
        
sum:  2323
