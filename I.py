from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())

if (a+b)<c or (b+c)<a or (a+c)<b:
    print("Incorrecto")
else:
    if a == b == c:
        print("Equilatero")
    if a != b != c:
        print("Escaleno")
    if a == b != c or a == c != b or b == c != a:
        print("Isosceles")
