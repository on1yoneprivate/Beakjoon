n = int(input())
input_list = list(map(int,input().split()))

def is_prime(x):
    if x < 2 :
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

count = 0
for num in input_list:
    if is_prime(num):
        count += 1

print(count)
