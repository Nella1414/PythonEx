from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())

v1a = a % 10
v2a = (a % 100)//10
v3a = (a % 1000)//100
v4a = (a % 10000)//1000
x = v1a + v2a + v3a + v4a


v1b = b % 10
v2b = (b % 100)//10
v3b = (b % 1000)//100
v4b = (b % 10000)//1000
y = v1b + v2b + v3b + v4b

if x == y:
    print(a, "y", b, "si son familia")
else:
    print(a, "y", b, "no son familia")
