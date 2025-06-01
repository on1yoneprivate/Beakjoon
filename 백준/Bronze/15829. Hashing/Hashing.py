import sys

input = sys.stdin.readline

l = int(input())
a = input().strip()
mod = 1234567891

result = 0
power = 1

for i in range(l):
    char = ord(a[i]) - 96       # 소문자 알파벳 a 아스키 코드 : 97
    result = (result + char * power) % mod
    power = (power * 31) % mod      # 지수 연산 누적 계산

print(result)