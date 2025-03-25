N = int(input())
point = 2   # 초기 한 변의 점 개수

# 반복할 때마다 한 변의 점의 개수가 2**i씩 증가
for i in range (N):
    point += 2**i

print(point**2)