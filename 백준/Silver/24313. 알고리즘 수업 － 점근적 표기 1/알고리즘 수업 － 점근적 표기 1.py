a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
    
flag = True

for n in range(n0, 201):  # n0 이상에서 모두 검사
    if a1 * n + a0 > c * n:
        flag = False
        break

print(1 if flag else 0)
