import sys

a = []

for i in range(3):
    x = sys.stdin.readline()

    x = x.strip()           # 줄바꿈 제거

    if x.isdigit():
        a.append(int(x))
    else:
        a.append(x)

count = 0           # 숫자가 몇 번째에 등장하는지
next = 0
for i in a:
    if isinstance(i, int):
        count = a.index(i)
        next = i + (3 - count)
    else:
        pass

if next % 3 == 0 and next % 5 == 0:
    print("FizzBuzz")
elif next % 3 == 0 and next % 5 != 0:
    print("Fizz")
elif next % 3 != 0 and next % 5 == 0:
    print("Buzz")
else:
    print(next)