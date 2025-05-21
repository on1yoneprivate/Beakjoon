while True:
    a = input()
    if a == '0':
        break
    if a == a[::-1]:  # 문자열을 뒤집어서 비교
        print("yes")
    else:
        print("no")
