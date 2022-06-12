from sys import stdin
a = int(stdin.readline())
v1a = ((a % 100) %10)
v2a = ((a % 1000) %100) // 10
v3a = ((a % 10000) %1000) // 100
v4a = ((a % 100000) %10000) // 1000

if v1a > v2a:
    if v1a > v3a:
        if v1a > v4a:
            print(v1a)

if v2a > v1a:
    if v2a > v3a:
        if v2a > v4a:
            print(v2a)

if v3a > v1a:
    if v3a > v2a:
        if v3a > v4a:
            print(v3a)

if v4a > v1a:
    if v4a > v2a:
        if v4a > v3a:
            print(v4a)
