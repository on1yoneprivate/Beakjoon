T = int(input())
costs = [int(input()) for _ in range(T)]

def calculate_change(cost):
    coin = []
    coin.append(cost // 25)             # quarter
    cost %= 25
    coin.append(cost // 10)             # dime
    cost %= 10
    coin.append(cost // 5)              # nickel
    cost %= 5
    coin.append(cost // 1)              # penny
    return coin

for cost in costs:
    print(*calculate_change(cost))