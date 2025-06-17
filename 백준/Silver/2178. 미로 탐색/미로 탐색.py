import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 이동할 수 있는 칸이고, 아직 방문하지 않은 칸일 경우
                if miro[nx][ny] == 1:
                    # 현재까지의 거리 + 1로 갱신 (이전 칸에서 한 칸 이동한 거리)
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))

    return miro[n-1][m-1]       # 최소 거리

print(bfs(0, 0))