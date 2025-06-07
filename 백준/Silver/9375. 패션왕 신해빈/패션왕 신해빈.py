import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    closet = {}

    for _ in range(n):
        name, category = input().split()

        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1

    result = 1
    for count in closet.values():
        result *= (count + 1)

    print(result - 1)           # 알몸인 상태 제외

