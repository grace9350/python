def fibonacci(n):
    if n == 0:
       list0[n] = 1
       list1[n] = 0
    elif n == 1:
        list1[n] = 1
        list0[n] = 0
    elif list0[n] == -1 | list1[n] == -1:
        fibonacci(n-1)
        fibonacci(n-2)
        list0[n] = list0[n-1] + list0[n-2]
        list1[n] = list1[n-1] + list1[n-2]
    

list0 = [-1 for i in range(41)]
list1 = [-1 for i in range(41)]

T = int(input())
for i in range(T):
    N = int(input())
    fibonacci(N)
    print(list0[N], list1[N])
