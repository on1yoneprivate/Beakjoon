s = input().upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = [0] * 26  # 사용된 단어 개수 배열 초기화
max_val = 0
max_idx = -1

for i in range(len(s)):
    # 사용된 단어의 개수 세기
    if s[i] in alphabet:
        idx = alphabet.find(s[i])
        result[idx] += 1

        # 가장 많이 사용된 알파벳, 해당 인덱스 저장
        if result[idx] > max_val:
            max_val = result[idx]
            max_idx = idx
        else:
            continue

    else :
        continue

# 가장 많이 사용된 알파벳의 개수가 여러 개일 경우 ? 출력
if result.count(max_val) > 1:
    print("?")
else:
    print(alphabet[max_idx])