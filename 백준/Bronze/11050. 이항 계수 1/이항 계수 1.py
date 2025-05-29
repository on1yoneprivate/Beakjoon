import sys

n, k = map(int, sys.stdin.readline().split())

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

# 조합 공식 : nCk = n!/(n-k)!k!
result = factorial(n) // (factorial(n-k) * factorial(k))

print(result)