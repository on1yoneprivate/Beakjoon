import sys

n, m = map(int, sys.stdin.readline().split())
n_set = set()
for i in range(n):
    n_set.add(sys.stdin.readline())

m_list = [] * m
for j in range(m):
    m_list.append(sys.stdin.readline())

count = 0
for a in m_list:
    if a in n_set:
        count += 1

print(count)