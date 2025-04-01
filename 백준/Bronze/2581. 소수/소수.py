import math

m = int(input())
n = int(input())
prime = []

def prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if prime_number(i):
        prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
