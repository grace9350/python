
#main
N = int(input()) #회사 수
a = [] #2차원리스트 a 생성
b = []
cnt = 1
idx = 0
for i in range(N): ##range(N)임 그냥 N아님
    #회사별 시작과 끝 시간 입력
    start, end = input().split()
    start = int(start)
    end = int(end)
    #i행 0열: start, i행 1열: end
    a.append([start, end])

a.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
     if i == 0:
        b.append(cnt)
    else if a[i][0] == a[i - 1][0]:
        b[idx]

#3차원 배열
#시작시간이 같은 것은 패스
max = 0
for i in range(N):
    cur = 0
    count = 0
    j = i
    while j < N:
        if cur < a[j][0]:
            cur = a[j][1]
            count += 1
        j += 1 ##j+=1은 if문 바깥에서! 공통 부분이므로
    if max < count:
        max = count

print(max)
            
