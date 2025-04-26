import sys

n = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

answer = []
for i in find:
    if i in card:       # 카드를 가지고 있을 경우
        answer.append(1)
    else:                   # 카드를 가지고 있지 않을 경우
        answer.append(0)

print(*answer)