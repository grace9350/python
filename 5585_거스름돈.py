price = int(input())
cnt = 0
price = 1000 - price #거스름돈이므로 1000엔에서 price 빼

if price >= 500:
    cnt += int(price / 500) #int로 바꾸지 않으면 소수점 발
    price = price % 500
    
if price >= 100:
    cnt += int(price / 100)
    price = price % 100
    
if price >= 50:
    cnt += int(price / 50)
    price = price % 50
   
if price >= 10:
    cnt += int(price / 10)
    price = price % 10
    
if price >= 5:
    cnt += int(price / 5)
    price = price % 5
   
if price >= 1:
    cnt += int(price / 1)
    price = price % 1
   
print(cnt)
    
