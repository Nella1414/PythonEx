from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())

if a < b:
    print("<")
if a > b:
    print(">")
if a == b:
    print("=")
