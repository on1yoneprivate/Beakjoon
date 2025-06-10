import sys
input = sys.stdin.readline

n = input().strip()

parts = n.split("-")        # - 기준으로 나누기

# - 나오기 전 값들은 모두 더함
_sum = sum(map(int, parts[0].split("+")))

# - 이후의 값들은 모두 괄호로 묶어서 빼기
for part in parts[1:]:
    _sum -= sum(map(int, part.split("+")))

print(_sum)