# 10개의 입력값을 배열로 생성
numbers = [int(input()) for i in range(10)]

remainder = []

# 중복된 나머지는 remainder 배열에 추가되지 않도록 함
for i in range(10):
    if numbers[i]%42 not in remainder:
        remainder.append(numbers[i]%42)

print(len(remainder))