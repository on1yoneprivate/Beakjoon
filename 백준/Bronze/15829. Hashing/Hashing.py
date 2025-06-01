import sys
import math

input = sys.stdin.readline

l = int(input())

a = input().rstrip()
arr = list(a)
num_arr = []

for i in arr:
    ans = ord(i) - 96       # 소문자 알파벳 a 아스키 코드 : 97
    num_arr.append(ans)

result = 0
for i in range(l):
    result += num_arr[i] * 31**i

print(result)