import sys

input = sys.stdin.readline

def is_balance(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()

    return not stack

while True:
    line = input()
    if not line:
        break
    raw_line = line.rstrip('\n')
    if raw_line == ".":
        break
    print("yes" if is_balance(raw_line) else "no")