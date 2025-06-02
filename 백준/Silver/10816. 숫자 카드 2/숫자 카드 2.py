import sys

input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))     # 숫자 카드에 적혀있는 정수

m = int(input())
key = list(map(int, input().split()))       # 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수

# 개수 세기
card_count = {}
for num in card:
    if num in card_count:
        card_count[num] += 1
    else:
        card_count[num] = 1

result = []
for k in key:
    result.append(card_count.get(k, 0))     # 없으면 0 반환

print(*result)