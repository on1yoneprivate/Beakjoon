import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_dic = {v:i for i, v in enumerate(sorted(set(n_list)))}

for i in range(n):
    print(n_dic[n_list[i]], end = ' ')