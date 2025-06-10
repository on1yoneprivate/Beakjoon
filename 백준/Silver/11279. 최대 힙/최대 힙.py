import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap) * -1)      # 가장 큰 값 꺼내기 (음수 -> 양수를 위해 -1을 곱함)
        else:
            print(0)        # 힙이 비어 있을 경우
    else:
        heapq.heappush(heap, x*(-1))         # 음수로 값을 저장 (최대힙)