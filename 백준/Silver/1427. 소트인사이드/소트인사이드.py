import sys

n = sys.stdin.readline()
arr = []

for i in range(len(n)-1):
    arr.append(n[i])

int_arr = list(map(int, arr))
int_arr.sort()
int_arr.reverse()

print(*int_arr, sep='')