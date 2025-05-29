import sys

input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append([x, y])

rate = [1]* n
for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rate[i] += 1

print(*rate)