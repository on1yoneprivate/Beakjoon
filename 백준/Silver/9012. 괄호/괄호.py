import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    test = input().strip()
    stack = 0
    is_vps = True

    for ch in test:
        if ch == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                is_vps = False
                break

    if stack != 0:
        is_vps = False

    print("YES" if is_vps else "NO")