n = int(input())
total_area = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            total_area[i][j] = 1

# 전체 면적 : 1로 표시된 칸 수
area = sum(sum(row) for row in total_area)
print(area)