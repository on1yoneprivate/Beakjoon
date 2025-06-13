import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

land = []
for _ in range(n):
    land.extend(list(map(int, input().split())))

min_time = float('inf')
target_height = 0

for h in range(257):        # 땅의 높이 : 최대 256
    time = 0
    inventory = b

    for height in land:
        # 현재 땅이 목표 높이보다 높으면 블록 제거
        if height > h:
            time += 2 * (height - h)        # 블록 제거 : 2초 소요
            inventory += (height - h)       # 제거된 블록의 수를 인벤토리에 추가
        elif height < h:
            time += 1 * (h - height)
            inventory -= (h - height)

    if inventory >= 0:
        if time < min_time:
            min_time = time
            target_height = h

        # 시간이 같으면 더 높은 높이를 선택
        elif time == min_time and h > target_height:
            target_height = h

print(min_time, target_height)