Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c=10
id(c)
1410890727952
type(c)
<class 'int'>
print(c)
10
2^13
15
bin(18)
'0b10010'
bin(0.023333)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    bin(0.023333)
TypeError: 'float' object cannot be interpreted as an integer
bin(2.3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    bin(2.3)
TypeError: 'float' object cannot be interpreted as an integer
type(0B000110)
<class 'int'>
int(0B000110)
6
float(1.00011001100)
1.000110011
type(1.0011001100)
<class 'float'>
0o(12)
SyntaxError: invalid octal literal
0O(12)
SyntaxError: invalid octal literal
oct(12)
'0o14'
oct(0B0101010)
'0o52'
oct(0X123)
'0o443'
hex(12)
'0xc'
c=1.2e3
print(c)
1200.0
a=19+2.3j
b=23+3.4j
c=a+b
print(c)
(42+5.699999999999999j)
type(c)
<class 'complex'>
c=1293.4j
c.real
0.0
c=23+4j
c.real
23.0
c.imaginary
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.imaginary
AttributeError: 'complex' object has no attribute 'imaginary'
"""jhggfwfguiwfhufh"""
'jhggfwfguiwfhufh'
a=("hello", "hello")
print(a)
('hello', 'hello')
a="hello"
print(a,"world")
hello world
a="""he"'ll'"o' "w'o"r'ld"""
a="hello"
print(a)
hello
"""slicing of tiring"""
'slicing of tiring'
a= "abcdefghhji"
for i in a:
    print(i)

    
a
b
c
d
e
f
g
h
h
j
i
s="vijay"
s[0]
'v'
s[-1]
'y'
s[40]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s[40]
IndexError: string index out of range
x=10
for i=1 i>0  i++
SyntaxError: invalid syntax
s="vijay"
s[1:40]
'ijay'
s[1:]
'ijay'
s[2:]
'jay'
s[:1]
'v'
s[:4]
'vija'
s[:]
'vijay'
s*3
'vijayvijayvijay'
len(s)
5
 f="hhhh
 
SyntaxError: unexpected indent
f="dhdh
SyntaxError: unterminated string literal (detected at line 1)
d="hdhu"
len(d)
4
a=10
b=10
id(a)
1410890727952
id(b)
1410890727952
x=[23,34,56,77]
type(x)
<class 'list'>
b=bytes(x)
print(b)
b'\x17"8M'
type(b)
<class 'bytes'>
x=[12,23,34,45]
print(b[0])1
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(b[0])
23
x=[10,20,30,40]
b=bytearay(c)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b=bytearay(c)
NameError: name 'bytearay' is not defined. Did you mean: 'bytearray'?
b=bytearray(x)
type(b)
<class 'bytearray'>
for i in b:
    print(i)

    
10
20
30
40
b[0]
10
