import sys

n = int(sys.stdin.readline())

a = []

for i in range(n):
    [xi, yi] = map(int,sys.stdin.readline().split())
    a.append([yi, xi])
a.sort()

for i in a:
    print(i[1], i[0])