import math

n = int(input())

def prime(m):
    answer = []
    x = 2
    while x <= m:
        if m % x == 0:
            answer.append(x)
            m //= x
        else:
            x += 1
    return answer

if n == 1:
    pass
else:
    result = prime(n)
    print(*result, sep='\n')
