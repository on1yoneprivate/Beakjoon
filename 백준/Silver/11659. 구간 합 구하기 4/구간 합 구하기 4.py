import sys

n, m = map(int, sys.stdin.readline().split())

n_list = list(map(int, sys.stdin.readline().split()))

# 누적합 배열
prefix_sum = [0]
for num in n_list:
    prefix_sum.append(prefix_sum[-1] + num)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])