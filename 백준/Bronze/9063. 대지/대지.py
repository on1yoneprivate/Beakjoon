n = int(input())
x = []
y = []

if n == 1:
    print(0)
else:
    for i in range(n):
        a, b = map(int,input().split())
        x.append(a)
        y.append(b)

    weight = max(x) - min(x)
    height = max(y) - min(y)

    print(weight * height)