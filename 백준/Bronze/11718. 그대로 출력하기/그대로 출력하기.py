while True:
    try:
        s = input()
        print(s)
    except EOFError:  # EOF (Ctrl+D 또는 Ctrl+Z 입력 시 종료)
        break
