from sys import stdin
a = int(stdin.readline())
b = float(stdin.readline())
if a == 1 or 2 or 3 or -1 or -2 or -3:
    if a == 1:
        print(b*500, "gr")
    if a == 2:
        print(b*100, "cm")
    if a == 3:
        print(b*0.62, "mi")
    if a == -1:
        print(b/500, "lb")
    if a == -2:
        print(b/100, "mt")
    if a == -3:
        print(b/0.62, "km")
