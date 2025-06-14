import sys
input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]

for i in range(n+1):

    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j*j] + 1)     # 최소 개수의 제곱수 합 구하기

print(dp[n])