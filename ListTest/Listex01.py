products = ['노트북', '마우스', '키보드', '모니터', '웹캠','마우스패드']
stocks = [15, 3, 8, 22, 5, 11]
num=0
total =0

items ={}
for item in products:
    items[item] = stocks[num]
    num+=1
print(items)

print("=== 재고 현황 ===")
for p in items.keys():
    print(f"{p} : {items[p]}개",end=" ")
    total += items[p]
    if items[p] < 10:
        print("재고 부족",end = " ")
    print()

print()
print(f"전체 재고 합계 : {total}개")




# f-String 사용하면 해결
# 출력하는 값을 담는 변수 msg이용해서 str()
# 파이썬은 문자와 숫자를 하나로 나열할 수 없다.
# 그러므로 str()함수를 이용해 숫자를 문자열로 변환하여 나열한다.
msg = products + ":" + str(stocks) + "개"






