A, B, C = map(int,input().split())
max = max(A, B, C)
if A == B == C:
    print(10000 + A*1000)
elif A == B or A == C:
    print(1000+ A*100)
elif B==C:
    print(1000+B*100)
elif A != B != C :
    print(100 * max)