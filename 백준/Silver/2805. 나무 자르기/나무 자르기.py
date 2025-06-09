import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    log = 0    # 나무의 총 길이
    
    for i in tree:
      if i > mid:
           log += i - mid
    if log < m:
      end = mid - 1
    else:
      start = mid + 1
    
print(end)