H, M = map(int,input().split())

if M < 45:
   H = 23 if H==0 else H-1
   M += 15
else:
    M -= 45
    
print(H, M)