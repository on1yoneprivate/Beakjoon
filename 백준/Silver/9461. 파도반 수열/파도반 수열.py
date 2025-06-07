import sys
input = sys.stdin.readline

t = int(input())
p = [0,1,1,1,2,2,3,4,5,7,9]

def getTriangle(n):
    for i in range(len(p), n+1):
        p.append(p[i-2] + p[i-3])

for i in range(t):
    num = int(input())
    if num < len(p):
        print(p[num])
    else:
        getTriangle(num)
        print(p[num])