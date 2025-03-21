grade = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
grade1_sum = 0.0
grade2_sum = 0.0

for i in range(20):
    s = input().split()
    # 학점의 총합
    grade1_sum += float(s[1])

    # 등급이 P인 과목은 계산에서 제외 -> 학점의 총합에서도 제외해야 함
    if s[2] == 'P':
        grade1_sum -= float(s[1])
    else:
        # 학점 x 과목 평점의 합
        grade2_sum += grade[s[2]] * float(s[1])

print(grade2_sum/grade1_sum)