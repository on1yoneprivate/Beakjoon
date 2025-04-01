x = int(input())

start = 1       # 시작 층
for i in range(1, x+1):
    if start <= x < start + i:
        n = x - start
        if i % 2 == 0:
            numer = 1 + n
            demon = i - n
        else:
            numer = i - n
            demon = 1 + n
        print(f"{numer}/{demon}")
        break
    start += i
