import sys

input = sys.stdin.readline

t = int(input())
dp = [(0, 0)] * 41      # N은 40보다 작거나 같은 자연수 또는 0

# 초기값
dp[0] = (1, 0)  # fibonacci(0)
dp[1] = (0, 1)  # fibonacci(1)

# dp 테이블 채우기
for i in range(2, 41):
    # fibonacci(i) = fibonacci(i-1) + fibonacci(i-2)
    zero_count = dp[i-1][0] + dp[i-2][0]
    one_count = dp[i-1][1] + dp[i-2][1]

    dp[i] = (zero_count, one_count)

for _ in range(t):
    n = int(input())

    print(dp[n][0], dp[n][1])