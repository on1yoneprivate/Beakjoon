A, B = input().split()

# 입력 받은 두 정수를 거꾸로 변경
reverse_a, reverse_b = int(str(A)[::-1]), int(str(B)[::-1])

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)