import sys

k = int(sys.stdin.readline())
j = []

for i in range(k):
    x = int(sys.stdin.readline())

    if x == 0:      # 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우기
        j.pop()
    else:           # 아닐 경우 해당 수를 쓴다.
        j.append(x)

print(sum(j))
