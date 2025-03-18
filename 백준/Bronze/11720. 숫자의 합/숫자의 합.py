N = int(input())
# 숫자 N개를 리스트 s로 생성
s = list(map(int,input()))

sum = 0
for i in range(len(s)):        # N개의 숫자 sum
    sum += s[i]

print(sum)