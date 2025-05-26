import sys

m = int(sys.stdin.readline())

s = set()
for i in range(m):
    cmd = sys.stdin.readline().rstrip().split()

    if len(cmd) == 1:
        cal = cmd[0]
    else:
        cal, num = cmd[0], int(cmd[1])

    if cal == "add":
        s.add(num)
    elif cal == "remove":
        s.discard(num)
    elif cal == "check":
        print(1 if num in s else 0)
    elif cal == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cal == "all":
        s = set(range(1,21))
    elif cal == "empty":
        s = set()
