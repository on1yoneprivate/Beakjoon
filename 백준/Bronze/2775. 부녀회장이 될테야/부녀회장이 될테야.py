import sys

t = int(sys.stdin.readline())

# 최대 층 수 14, 최대 호 수 14
dp = [[0] * 15 for _ in range(15)]

# 0층 초기화
for i in range(1, 15):
    dp[0][i] = i

# dp 테이블
for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]      # n층 k호

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(dp[k][n])