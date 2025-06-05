import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
ans = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(i // mid for i in lan)

    if count >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)