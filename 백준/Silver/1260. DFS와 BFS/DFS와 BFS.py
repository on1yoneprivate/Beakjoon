import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True       # 현재 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]:      # 현재 노드에 연결된 노드들 중에서 방문하지 않은 노드가 있다면 dfs 재귀 호출
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = [v]     # 탐색 시작 노드를 큐에 삽입

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)            # 방문 처리 (리스트에 추가)
            queue.extend(graph[node])       # 현재 노드에 연결된 노드들을 큐에 추가

    print(*visited)


visited_dfs = [False] * (n+1)
dfs(graph, v, visited_dfs)
print()

visited_bfs = []
bfs(graph, v, visited_bfs)