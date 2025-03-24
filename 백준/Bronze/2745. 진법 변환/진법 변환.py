N, B = input().split()
result = 0

for i in range(len(N)):
    c = N[-(i+1)]   # 역순으로 조회
    if c.isdigit():
        value = int(c)
    else:
        value = ord(c) - ord('A') + 10

    result += (int(B)**i) * value

print(result)
