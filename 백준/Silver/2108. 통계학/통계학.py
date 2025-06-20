import sys
input = sys.stdin.readline

n = int(input())
data = []

_sum = 0
count = dict()
for _ in range(n):
    x = int(input())
    data.append(x)

    _sum += x

    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

data.sort()

# 산술 평균
print(round(_sum/n))

# 중앙값
print(data[n//2])

# 최빈값
mode = max(count.values())
numbers = []
for key, value in count.items():
    if value == mode:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

# 범위
print(data[-1] - data[0])