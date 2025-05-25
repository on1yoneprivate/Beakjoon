import sys

n, m = map(int, sys.stdin.readline().split())

n_dict = {}
for i in range(n):
    site, pw = sys.stdin.readline().split()
    n_dict[site] = pw

for _ in range(m):
    find = sys.stdin.readline().rstrip()
    print(n_dict[find])