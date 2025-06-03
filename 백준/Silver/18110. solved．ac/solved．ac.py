import sys

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()

level = [int(input()) for _ in range(n)]
level.sort()

trimmed = int(n * 0.15 + 0.5)  # 절사 개수
level = level[trimmed:n - trimmed]

if not level:  # 리스트가 비어 있을 경우
    print(0)
else:
    # 절사 평균
    mean = sum(level) / len(level)
    print(int(mean + 0.5))