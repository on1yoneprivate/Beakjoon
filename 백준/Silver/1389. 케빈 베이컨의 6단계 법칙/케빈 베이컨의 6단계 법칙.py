import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for friend in graph[current]:
            if not visited[friend]:
                visited[friend] = True
                distance[friend] = distance[current] + 1
                queue.append(friend)

    return sum(distance)

min_total = float('inf')
answer = 0

for i in range(1, n+1):
    total = bfs(i)
    if total < min_total:
        min_total = total
        answer = i

print(answer)