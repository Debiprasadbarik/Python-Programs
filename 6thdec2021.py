Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list=[12,10.5,'Debi',True]
print(list[1])
10.5
print(list[2])
Debi
list=[10,20,30,40]
print(list[0])
10
list[1]
20
list[-1]
40
list[1:3]
[20, 30]
list[0]
10
list[23]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list[23]
IndexError: list index out of range
list[-6]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list[-6]
IndexError: list index out of range
list=[10,20,30]
list.append("Debi")
for i in list
SyntaxError: expected ':'
print(list[])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
list
[10, 20, 30, 'Debi']
list.remove(20)
list
[10, 30, 'Debi']
list=[10,20,30]
list.append("vijay")
list
[10, 20, 30, 'vijay']
list2=list*2
list2
[10, 20, 30, 'vijay', 10, 20, 30, 'vijay']
