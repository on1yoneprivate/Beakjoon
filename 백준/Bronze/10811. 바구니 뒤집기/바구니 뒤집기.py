N, M = map(int,input().split())

numbers = [num for num in range(1,N+1)]

for _ in range(M):
    i, j = map(int,input().split())
    # i번째 바구니부터 j번째 바구니의 순서 역순으로 정렬
    numbers[i-1:j] = numbers[i-1:j][::-1]
        

print(" ".join(map(str, numbers)))