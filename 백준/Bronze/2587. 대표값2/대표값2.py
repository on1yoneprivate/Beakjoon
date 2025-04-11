a = []
sum = 0

for i in range(5):
    x = int(input())
    a.append(x)
    sum += x

a.sort()

print(sum//5)       # 평균 출력
print(a[2])         # 중앙값 출력