N, M = map(int, input().split())

A = []
B = []

# 행렬 A 입력 받기 (N개의 행)
for _ in range(N):
    A.append(list(map(int, input().split())))

# 행렬 B 입력 받기 (N개의 행)
for _ in range(N):
    B.append(list(map(int, input().split())))

# 행렬의 합 계산 및 출력
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
