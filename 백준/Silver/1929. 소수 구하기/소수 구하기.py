import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def is_prime(x : int) -> bool:
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

for x in range(n, m+1):
    if is_prime(x):
        print(x)