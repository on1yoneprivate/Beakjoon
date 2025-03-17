# 30명의 출석 번호(1번~30번) 생성
students = [i for i in range(1,31)]

# 과제를 제출 한 28명 제거
for _ in range(28):
    students.remove(int(input()))

# 과제 미제출자 2명 정렬 후 출력
not_submit = sorted(students)
print(not_submit[0])
print(not_submit[1])