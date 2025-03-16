N = int(input())
numbers = list(map(int,input().split()))

max_val, min_val = numbers[0], numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    elif num < min_val:
        min_val = num
        
print(min_val, max_val)