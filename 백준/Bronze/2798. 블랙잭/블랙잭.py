from itertools import combinations

n, m = map(int,input().split())
c = list(map(int,input().split()))
result = 0

for i in combinations(c, 3):
    if sum(i) <= m:
        result = max(result, sum(i))

print(result)