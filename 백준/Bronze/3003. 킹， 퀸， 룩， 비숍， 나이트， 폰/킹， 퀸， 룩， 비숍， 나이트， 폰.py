chess = [1, 1, 2, 2, 2, 8]     # King, Queen, Rook, Bishop, Knight, Pawn
found = list(map(int,input().split()))    # 동혁이가 발견한 흰색 피스의 개수
result = [chess[i] - found[i] for i in range(6)]

print(*result)