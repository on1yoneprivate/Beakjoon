import sys

n = int(sys.stdin.readline())

record = {}
for i in range(n):
    name, status = sys.stdin.readline().split()
    record[name] = status

now = []
for key, value in record.items():
    if value == 'enter':
        now.append(key)

now.sort(reverse=True)
for i in now:
    print(i)