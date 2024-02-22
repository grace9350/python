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
