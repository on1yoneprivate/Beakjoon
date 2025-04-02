a, b, c = map(int,input().split())

triangle = [a, b, c]
max_value = max(triangle)
triangle.remove(max_value)

# 입력 받은 세 막대로 삼각형을 만들 수 있는 경우
if triangle[0] + triangle[1] > max_value:
    print (a+b+c)
# 막대의 길이 조절이 필요할 경우
# 삼각형의 조건에 맞도록 가장 큰 막대를 [나머지 두 변의 합 - 1]의 길이만큼 설정함 (삼각형의 둘레를 최대 조건 충족)
else:
    print((triangle[0]+triangle[1])*2 - 1 )