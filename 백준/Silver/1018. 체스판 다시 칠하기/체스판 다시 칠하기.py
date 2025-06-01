import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 기준 패턴
pattern1 = ['WBWBWBWB', 'BWBWBWBW']
pattern2 = ['BWBWBWBW', 'WBWBWBWB']

min_repaint = float('inf')  # 무한대로 설정 (처음에는 어떤 값보다도 크도록)

for i in range(n-7):
    for j in range(m-7):
        repaint1 = 0        # start : W
        repaint2 = 0        # start : B

        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != pattern1[x % 2][y]:
                    repaint1 += 1
                if board[i + x][j + y] != pattern2[x % 2][y]:
                    repaint2 += 1

        min_repaint = min(min_repaint, repaint1, repaint2)

print(min_repaint)