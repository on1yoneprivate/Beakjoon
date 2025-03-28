def findDivisor(n):
    divisorList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i) == 0:
            divisorList.append(i)
            if ( (i**2) != n ):
                divisorList.append(n//i)
    divisorList.sort()

    if len(divisorList) >= k:
        print(divisorList[k-1])
    else:
        print("0")

n, k = map(int,input().split())

findDivisor(n)