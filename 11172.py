from sys import stdin
cnt = int(stdin.readline())
n = 1

while n<=cnt:
    lin1 = stdin.readline()
    lin2 = lin1.split()
    n1 = int(lin2[0])
    n2 = int(lin2[1])
    if n1 > n2:
        print(">")
    if n1 < n2:
        print("<")
    if n1 == n2:
        print("=")
        
    n +=1
