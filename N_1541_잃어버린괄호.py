#입력받은것을 -기준으로 나누어 리스트에 저장
list1 = input().split('-')
cnt = 0
min = 0
for i in list1:
    #list1의 원소를 +기준으로 나누어 리스트에 저장
    list2 = i.split('+')
    sum = 0
    for j in list2:
        #list2의 원소를 모두 더하기
        sum += int(j)
    if cnt == 0:
        min += sum
    else:
        min -= sum
    cnt+=1
print(min)

#마이너스(-)단위로 나누어야 함
#리스트 안의 원소는 숫자와 플러스(+)로 이루어진 문자열 => 모두 더하기
#첫번째 원소는 양수이고, 두번째 원소부터는 음수임

