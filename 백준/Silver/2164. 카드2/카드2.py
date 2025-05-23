import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(range(1, n+1))

while len(card) > 1:
    card.popleft()              # 제일 위 카드 버리기
    card.append(card.popleft())     # 제일 위 카드를 맨 아래로 이동

print(card[0])