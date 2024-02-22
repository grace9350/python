N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum = 0
min = 0
for i in range(N):
    sum += arr[i]
    min += sum
print(min)
