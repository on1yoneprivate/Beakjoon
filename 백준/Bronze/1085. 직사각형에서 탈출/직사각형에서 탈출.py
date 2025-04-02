x, y, w, h = map(int,input().split())

if abs(x - w) > abs(x - 0):
    min_x = abs(x - 0)
else:
    min_x = abs(x - w)

if abs(y - h) > abs (y - 0):
    min_h = abs(y - 0)
else:
    min_h = abs(y - h)

if min_x < min_h:
    print(min_x)
else:
    print(min_h)