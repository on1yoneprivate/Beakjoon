import sys
import math

n = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
t, p = map(int,sys.stdin.readline().split())

shirt = 0
for i in size:
    shirt += math.ceil(i/t)
print(shirt)

count = n // p
each = n % p
print(count, each)