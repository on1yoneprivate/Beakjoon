import sys
input = sys.stdin.readline

n = int(input())

def count_2n(num):
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1

    for i in range(2, num+1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    return dp[num]

print(count_2n(n) % 10007)