N, M = map(int,input().split())

number = [i for i in range(N+1)]    # 각 바구니에 번호 저장
    
for _ in range (M):
    i, j = map(int,input().split())
    number[i], number[j] = number[j], number[i]

print(" ".join(map(str, number[1:])))