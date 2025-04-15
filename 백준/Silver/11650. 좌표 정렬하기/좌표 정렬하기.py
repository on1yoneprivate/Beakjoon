import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    [xi, yi] = map(int,sys.stdin.readline().split())
    a.append([xi, yi])
a.sort()

for i in a:
    print(i[0], i[1])
