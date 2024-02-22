def tile(n):
    if n == 1:
        listN[n] = 1
        return 1
    if n == 2:
        listN[n] = 2
        return 2
    if listN[n] == 0:
        listN[n] = tile(n-1)+tile(n-2)
        return listN[n]
    else:
        return listN[n]

n = int(input())
listN = [0 for i in range(n + 1)]

result = tile(n) % 10007
print(result)

# tile(n) = tile(n-1) + tile(n-2) !!
