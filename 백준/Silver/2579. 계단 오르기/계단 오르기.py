import sys

input = sys.stdin.readline
n = int(input())

score = [int(input()) for _ in range(n)]
dp = [0] * n     # n개의 계단

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, n):
        # 두 게단 전에서 바로 오를 경우 : dp[i-2]
        # 한 계단 전(i-1)을 밟았다면, i-2는 밟지 못함 : dp[i-3] + score[i-1]
        dp[i] = score[i] + max(dp[i-2], dp[i-3] + score[i-1])

    print(dp[n-1])