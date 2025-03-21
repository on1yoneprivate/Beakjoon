s = input()
sum = 0

for i in range(len(s)):
    if s[i].isalpha() == True:
        match s[i]:
            case 'z':
                # index가 0, i+1일 경우 indexError 발생하여 조건 수정
                if i > 0 and i+1 < len(s) and s[i-1] == 'd' and s[i+1] == '=':
                    continue
                else:
                    sum += 1
            case 'j':
                if i > 0 and (s[i-1] == 'n' or s[i-1] == 'l'):
                    continue
                else:
                    sum += 1
            case _ :
                sum += 1

print(sum)