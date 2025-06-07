import sys
input = sys.stdin.readline

t = int(input())
def count_cases(n):
    dp = [0] * (max(4, n+1))
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

for _ in range(t):
    num = int(input())
    print(count_cases(num))