import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif command[0] == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
