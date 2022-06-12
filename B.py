from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = stdin.readline()
d = c.strip()
if d == '+' or '-':
    if d == '+':
        print(a+b)
    if d == '-':
        print(a-b)

    
