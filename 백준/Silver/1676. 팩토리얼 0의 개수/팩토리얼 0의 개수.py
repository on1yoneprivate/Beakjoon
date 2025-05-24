import sys

#  끝자리 0은 2x5할 경우 생성됨
#  끝자리 0 개수 = 5의 배수가 몇 번 나왔는지
def count_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


n = int(sys.stdin.readline())
print(count_zeros(n))