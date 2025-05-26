import sys

n, m = map(int, sys.stdin.readline().split())

n_set = set(sys.stdin.readline().strip() for _ in range(n))
m_set = set(sys.stdin.readline().strip() for _ in range(m))

nm = n_set.intersection(m_set)
nm = sorted(nm)

print(len(nm))
for i in range(len(nm)):
    print(nm[i])