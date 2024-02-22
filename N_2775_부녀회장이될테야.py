"""def apartment(k, n):
    if k>0 & listN[k][n] == 0:
        for i in range(n + 1):
            apartment(k-1, i)
        sum = 0
        for i in range(n + 1):
            sum += listN[k-1][i]
        listN[k][n] = sum
       
listN = [[i+1 for i in range(14)]]
row = 0

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input()) - 1
    if row < k:
        for j in range(k - row):
            listN.append([0 for k in range(14)])
        row = k
    apartment(k, n)
    print(listN[k][n])
"""
#시간초과

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    listN = [j+1 for j in range(n)]

    for s in range(k):
        for t in range(1, n):
            listN[t] += listN[t-1]
        #print(listN)
    print(listN[n-1])

# 2차원 배열 쓰지 않고 1차원 배열 원소들 갱신
