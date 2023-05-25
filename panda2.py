import numpy as np

# 1.
a = []
b = []
b1 = []
b2 = []
# b3 = []
c5 = []
c6 = []
j = []
p = []
# sum1 = c = b = 0
# for i in range(10, 51):
#     if i % 3 == 0 or i % 5 == 0:
#         a.append(i)
#         c += 1
# q = np.array(a)
# r = len(q)
# d = r - 2
# print(q)
# for i in q[1: r - 1]:
#     b += i
# avg = b / d
# print(b)
# print(avg)


# 2.
# for i in range(10, 51):
#     if i % 2 == 0 and i % 5 == 0:
#         a.append(i)
# b = np.array(a)
# print(b)


# 3.
for i in range(2):
    b = input("Name:-")
    a.append(b)
c = np.array(a)
print(c)
for j in range(2):
    b1 = int(input("Roll No.:-"))
    b2.append(b1)
c1 = np.array(b2)
print(c1)
for i in range(2):
    b2 = float(input("Mark:-"))
    c5.append(b2)
c2 = np.array(c5)
print(c2)
for i in range(2):
    b2 = float(input("Mark:-"))
    c6.append(b2)
c3 = np.array(c6)
print(c3)
for i in range(2):
    b3 = float(input("Mark:-"))
    j.append(b3)
c4 = np.array(j)
print(c4)
for i in range(2):
    b2 = float(input("Mark:-"))
    p.append(b2)
c5 = np.array(p)
print(c5)
s = np.array([c], [c1], [c2], [c3], [c4], [c5])
print(s)

# family = np.dtype([('Name', 'S20'), ('Age', 'i8'), ('Mark', 'f8')])
# c = np.array([('samikshya', 19, 100), ('debidutta', 19, 101), ('dekshya', -8, 99), ('sonaxi', -9, 98)], dtype=family)
# print(c)
# a = np.dtype([('c', 'S20'), ('c1', 'i8'), ('c2', 'f8'), ('c3', 'f8'), ('c4', 'f8'), ('c5', 'f8')])
# c = np.array([a], [b], [c], [c1], [j], [p], dtype=a)
# print(c)
