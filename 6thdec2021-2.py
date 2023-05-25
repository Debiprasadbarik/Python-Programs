Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c=list(range(100))
print(c)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
for i in c:
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
list=[12,23,34]
list.append("debi")
list
[12, 23, 34, 'debi']
list[1]="debi"
list
[12, 'debi', 34, 'debi']
list.remove(23)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list.remove(23)
ValueError: list.remove(x): x not in list
list.remove(12)
list
['debi', 34, 'debi']
help(set)


help(set())


s={100,20,39,'debi'}
print(s)
{100, 20, 'debi', 39}
s={12,13,14,12,'debi',37,45,99,99}
s
{99, 45, 37, 'debi', 12, 13, 14}
s.add(100)
s
{99, 45, 37, 100, 'debi', 12, 13, 14}
s.remove(99)
print(s)
{45, 37, 100, 'debi', 12, 13, 14}
type(s)
<class 'set'>
s.assending
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.assending
AttributeError: 'set' object has no attribute 'assending'
s={10,20,30,40}
fs=frozenset(s)
print(fs)
frozenset({40, 10, 20, 30})
type(fs)
<class 'frozenset'>
<class 'frozenset'>
SyntaxError: invalid syntax
fs.append(21)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    fs.append(21)
AttributeError: 'frozenset' object has no attribute 'append'
fs.add(21)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    fs.add(21)
AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(21)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    fs.remove(21)
AttributeError: 'frozenset' object has no attribute 'remove'
l=list(range(1000))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l=list(range(1000))
TypeError: 'list' object is not callable
l=list(range(1000))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    l=list(range(1000))
TypeError: 'list' object is not callable
d={101:'vijay',102:'ravi',103:'debi'}
d[103]
'debi'
type(d)
<class 'dict'>
d['a']='apple'
print(d)
{101: 'vijay', 102: 'ravi', 103: 'debi', 'a': 'apple'}
d[101]='debi'
print(d)
{101: 'debi', 102: 'ravi', 103: 'debi', 'a': 'apple'}
d.remove(101)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d.remove(101)
AttributeError: 'dict' object has no attribute 'remove'
#important
help(dict())
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If the key is not found, return the default if given; otherwise,
 |      raise a KeyError.
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

KeyboardInterrupt
del d[108]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    del d[108]
KeyError: 108
del d[102]
d
{101: 'debi', 103: 'debi', 'a': 'apple'}
d.pop(101['debi'])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    d.pop(101['debi'])
TypeError: 'int' object is not subscriptable
a='it's beautiful day'
SyntaxError: unterminated string literal (detected at line 1)
a='it\'s a bautiful day'
a
"it's a bautiful day"
# MAX_VALUE=10
for i in r: