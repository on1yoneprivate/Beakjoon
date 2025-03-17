N = int(input())
now = list(map(int,input().split()))

M = max(now)
new_score = 0
for i in range(len(now)):
    new_score += now[i]/M*100

print(new_score/N)