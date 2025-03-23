A = list()
length = -1

for i in range(5):
    A.append(list(input()))
    if length < len(A[i]):
        length = len(A[i])

read = ''
# 세로로 읽은 순서대로 글자들을 출력
for i in range(length):
    for j in range(5):
        try:
            read = read + A[j][i]
        except:
            read = read + ''
print(read)