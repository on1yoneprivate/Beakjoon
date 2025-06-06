import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

com = int(input())
x = int(input())        # 연결 쌍

graph = [[] for _ in range(com+1)]
for _ in range(x):
    a, b = map(int, input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (com+1)       # 방문 노드 저장

dfs(graph, 1, visited)

print(visited.count(True) - 1)