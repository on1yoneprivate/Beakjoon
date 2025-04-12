import sys

n = int(sys.stdin.readline())
end = 666
count = 0

while True:
    if '666' in str(end):
        count += 1
        if count == n:
            print(end)
            break
    end += 1