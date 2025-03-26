import math

A, B, V = map(int,input().split())

# (다음 날 정상에 도달하기 위한 최소 높이) / (하루마다 올라가는 높이)) + 하루
day = ((V-A) / (A-B)) + 1

print(math.ceil(day))