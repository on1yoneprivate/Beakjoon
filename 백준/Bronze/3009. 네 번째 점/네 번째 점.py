a, b = map(int,input().split())
c, d = map(int,input().split())
e, f = map(int,input().split())

x = [a, c, e]
y = [b, d, f]

new_x= []
new_y = []
same_x = []
same_y = []

for i in x:
    if i not in new_x:
        new_x.append(i)
    else:
        if i not in same_x:
            same_x = i

for j in y:
    if j not in new_y:
        new_y.append(j)
    else:
        if j not in same_y:
            same_y = j

for k in x:
    if k != same_x:
        fourth_x = k
for k in y:
    if k != same_y:
        fourth_y = k

print(fourth_x, fourth_y)