from string import ascii_lowercase

N = int(input())

for i in range(N):
    s = input()
    alpha = list(ascii_lowercase)   # 소문자 알파벳 리스트 생성
    for j in range(len(s)) :
        if s[j] in alpha:
            if j == (len(s)-1) :    # 마지막 문자일 경우
                alpha.remove(s[j])
            elif s[j+1] == s[j]:    # 현재 알파벳과 다음 알파벳이 같을 경우
                continue
            elif s[j+1] != s[j]:    # 현재 알파벳과 다음 알파벳이 다를 경우
                alpha.remove(s[j])
        elif s[j] not in alpha:
            N -= 1
            break

print(N)
