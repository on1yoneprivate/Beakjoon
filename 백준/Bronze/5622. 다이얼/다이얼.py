s = input()
t = 1*len(s)

for i in s:
    if i == 'A' or i == 'B' or i == 'C':
        t += 2
    elif i == 'D' or i == 'E' or i == 'F':
        t += 3
    elif i == 'G' or i == 'H' or i == 'I':
        t += 4
    elif i == 'J' or i == 'K' or i == 'L':
        t += 5
    elif i == 'M' or i == 'N' or i == 'O':
        t += 6
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        t += 7
    elif i == 'T' or i == 'U' or i == 'V':
        t += 8
    elif i == 'X' or i == 'W' or i == 'Y' or i == 'Z':
        t += 9

print(t)