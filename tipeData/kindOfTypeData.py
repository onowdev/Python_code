a = "Hello World"
b = 20
c = 90.99
d = 9j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(6)
h = {"name" : "Agus", "age" : 34}
i = frozenset({"apple", "banana", "cherry"})
j = True
k = b"hello"
l = bytearray(8)
m = memoryview(bytes(7))
n = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

"""
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
"""

x = str("Hello world")
print(x)