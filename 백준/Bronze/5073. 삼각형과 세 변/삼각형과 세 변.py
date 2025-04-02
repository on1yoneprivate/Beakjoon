while True:
    a, b, c = map(int,input().split())
    triangle = [a, b, c]
    max_value = max(a, b, c)
    triangle.remove(max_value)

    if a == b == c == 0:
        break
    elif triangle[0] + triangle[1] > max_value:
        if a == b == c:
            print("Equilateral")
        elif a != b and a != c and b != c:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")