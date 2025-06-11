import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True

    for i in range(4):      # 네 방향에 대해서 방문
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동할 위치가 농장 범위 내라면
        if 0 <= nx < m and 0 <= ny < n:
            # 배추가 있고, 아직 방문하지 않았다면
            if farm[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    farm = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    count = 0       # 필요한 지렁이 수

    for y in range(n):
        for x in range(m):
            # 배추가 심어져 있고, 아직 방문하지 않았다면
            if farm[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1

    print(count)