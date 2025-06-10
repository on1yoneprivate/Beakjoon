import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:      # 힙이 비어 있으면 0 출력
        if heap:
            print(heapq.heappop(heap))      # 가장 작은 값 꺼내기
        else:
            print(0)        # 힙이 비어 있을 경우
    else:
        heapq.heappush(heap, x)         # 값 추가