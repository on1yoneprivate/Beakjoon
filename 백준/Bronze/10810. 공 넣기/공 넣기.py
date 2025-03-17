N, M = map(int,input().split())
numbers = [0] * (N + 1)    # 바구니에 들어 있는 번호 : 0으로 초기화

for _ in range (M):
    i, j, k = map(int,input().split())
    for a in range(i, j+1):    # i번 바구니 ~ j번 바구니까지 번호 변경
        numbers[a] = k
    
print(" ".join(map(str, numbers[1:])))