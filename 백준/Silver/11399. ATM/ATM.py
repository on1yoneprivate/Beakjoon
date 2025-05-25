import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))
p.sort()

time = []
for i in range(1, n+1):
    time.append(sum(p[:i]))     # 각 사람의 누적합 구하기

print(sum(time))