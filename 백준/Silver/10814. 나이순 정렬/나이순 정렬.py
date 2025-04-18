import sys

n = int(sys.stdin.readline())
member = []

for i in range(n):
    [age, name] = sys.stdin.readline().split()
    member.append([int(age), name])

# 나이순 정렬
member.sort(key=lambda x:x[0])

for i in range(n):
    print(member[i][0], member[i][1])