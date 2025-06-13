import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001

q = deque()
q.append((n, 0))        # 현재 위치, 소요 시간
visited[n] = False

while q:
    pos, sec = q.popleft()
    if pos == k:
        print(sec)
        break
    for next_pos in [pos-1, pos+1, pos*2]:          # 이동 가능 범위 : -1, +1, *2
        if 0 <= next_pos < 100001 and not visited[next_pos]:
            q.append((next_pos, sec+1))
            visited[next_pos] = True