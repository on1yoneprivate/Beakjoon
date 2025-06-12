import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

# 슬라이딩 윈도우 변수 초기화
start = 0
end = 0
max_length = 0
fruit_count = defaultdict(int)

while end < N:
    fruit_count[fruits[end]] += 1  # 현재 과일 추가

    # 과일 종류가 2개 초과일 경우, start를 오른쪽으로 이동
    while len(fruit_count) > 2:
        fruit_count[fruits[start]] -= 1
        if fruit_count[fruits[start]] == 0:
            del fruit_count[fruits[start]]
        start += 1

    # 조건 만족: 현재 윈도우 길이로 최대값 갱신
    max_length = max(max_length, end - start + 1)

    end += 1  # 윈도우 오른쪽 확장

print(max_length)
