import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(range(1, n + 1))

result = []
idx = 0

while s:
    idx = (idx + k - 1) % len(s)        # 다음에 제거할 인덱스
    result.append(s.pop(idx))           # 해당 인덱스 제거

print("<" + ", ".join(map(str, result)) + ">")