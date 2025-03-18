s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = [-1] * 26         # 결과값 -1로 초기화

for i in range (len(s)):
    if s[i] in alphabet:
        idx = alphabet.find(s[i])
        # 처음 등장하는 위치를 출력하기 위해 if문 사용
        if result[idx] == -1:
            result[idx] = i
        else:
            continue

print(*result)