import sys

n, m = map(int, sys.stdin.readline().split())

# 포켓몬 도감 생성 : 도감 번호는 1부터 시작
pokemon = [None] + [sys.stdin.readline().strip() for _ in range(n)]
# key : 이름, value : 도감 번호
p_dict = { name : str(i) for i, name in enumerate(pokemon) if i != 0 }

for _ in range(m):
    test = sys.stdin.readline().strip()

    if test.isdigit():
        print(pokemon[int(test)])

    else:
        print(p_dict[test])