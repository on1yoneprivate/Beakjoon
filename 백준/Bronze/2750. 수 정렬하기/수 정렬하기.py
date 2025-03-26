N = int(input())

previous = []

for i in range(N):
    previous.append(int(input()))

previous.sort()
for _ in range(N):
    print(previous[_])