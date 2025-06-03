import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))

    queue = [(i, p) for i,p in enumerate(weight)]       # (인덱스, 중요도)
    count = 0       # 인쇄 순서

    while queue:
        current = queue[0]
        if any(current[1] < q[1] for q in queue[1:]):
            queue.append(queue.pop(0))      # 맨 앞을 맨 뒤로 보냄
        else:
            queue.pop(0)        # 인쇄
            count += 1
            if current[0] == m:
                print(count)
                break