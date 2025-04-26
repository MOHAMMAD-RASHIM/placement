val=[6,7,1,3,8,2,5]

def maxStolenValue(val):
    n = len(val)
    if n == 0:
        return 0
    if n == 1:
        return val[0]
    
    DP=[0]*n
    DP[0]=max(DP[0],DP[1])
    # DP[1]=max(DP[0],DP[1])
    for index in range(1,n):
        DP[index]=max(DP[index-1],DP[index-2]+val[index])
        print(DP)
    return DP[-1]

print(maxStolenValue(val))