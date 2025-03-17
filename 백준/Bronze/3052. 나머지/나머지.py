# 10개의 입력값을 배열로 생성
numbers = [int(input()) for i in range(10)]

# 중복되는 나머지 값은 한 번만 저장
remainder = set()

# 42로 나눈 나머지를 집합에 추가
for num in numbers:
    remainder.add(num % 42)
    
print(len(remainder))