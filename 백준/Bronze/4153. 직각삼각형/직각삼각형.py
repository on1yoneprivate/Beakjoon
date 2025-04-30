import sys

while 1:
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == a[1] == a[2] == 0:
        break

    max_value = max(a)
    a.remove(max_value)
    if max_value**2 == (a[0]**2 + a[1]**2):
        print('right')
    else:
        print('wrong')