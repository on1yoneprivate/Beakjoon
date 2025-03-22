A = []
max_val = -1
location = [0, 0]
# 9 x 9 행렬 A
for i in range(9):
    A.append(list(map(int, input().split())))

# 행렬의 합 계산
for i in range(9):
    for j in range(9):
        if A[i][j] > max_val:
            max_val = A[i][j]
            # 최댓값이 위치한 행 번호와 열 번호 인덱스 변경
            location[0], location[1] = i+1, j+1

print(max_val)
print(*location)