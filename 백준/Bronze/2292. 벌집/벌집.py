N = int(input())

a = 1
count = 1

while N > a:
    a += 6 * count
    count += 1

print(count)