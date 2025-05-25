import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
coin.sort(reverse=True)

count = 0
for c in coin:
    if k >= c:
        count += k // c
        k %= c

print(count)