import sys
input = sys.stdin.readline

n = int(input())
stack, ans = [], []
find = True

now = 1
for _ in range(n):
    num = int(input())

    # push
    while now <= num:
        stack.append(now)
        ans.append("+")
        now += 1

    # pop
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:       # 불가능한 경우
        find = False

if not find:
    print("NO")
else:
    for i in ans:
        print(i)