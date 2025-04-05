n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))   # i의 각 자릿수 합
    num_sum = num + i       # 분해합 = 생성자 + 각 자릿수의 합
    if num_sum == n:
        print(i)
        break
    if i == n:                      # 생성자가 없을 경우
        print(0)