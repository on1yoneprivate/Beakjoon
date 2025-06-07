import sys
input = sys.stdin.readline

n = int(input())

def count_2n(num):
    dp = [0] * (max(4, n+1))
    dp[1], dp[2], dp[3] = 1, 2, 3

    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[num]

print(count_2n(n) % 10007)

