qr_code = "0123456789ABCDEFGHIJKLMNOPORSTUVWXYZ\$%*+-./:"

T = int(input())        # 테스트 케이스 개수 입력

for t in range (T):
    result = []
    R, S = input().split()    # R : 반복 횟수(정수), S : 문자열
    R = int(R)
    for i in S:
            result.append(i*R)
            
    print("".join(result))