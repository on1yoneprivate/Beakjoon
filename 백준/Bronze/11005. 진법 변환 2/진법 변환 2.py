N, B = map(int,input().split())

# 2/8/16 진수 : 내장함수 사용
if B == 2:
    print(bin(N)[2:])   # 0b 제거
elif B == 8:
    print(oct(N)[2:])   # 0o 제거
elif B == 16:
    print(hex(N)[2:].upper())   # 0x 제거
else:
    result = ""
    while N > 0:
        q, r = divmod(N, B)
        if r > 9:
            # 나머지를 역순으로 모으기
            result = chr(r+55) + result
        else:
            result = str(r) + result
        N = q
    print(result)