import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global count
    visited[y][x] = True

    if school[y][x] == 'P':
        count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내 방문 + 벽이 아닐 경우
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and school[ny][nx] != 'X':
                dfs(nx, ny)

n, m = map(int, input().split())
school = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 도연이 위치 찾기
for i in range(n):
    for j in range(m):
        if school[i][j] == 'I':
            start_x, start_y = j, i
            break

count = 0
dfs(start_x, start_y)

print(count if count > 0 else "TT")