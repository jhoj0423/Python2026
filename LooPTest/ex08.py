target = int(input("목표 일 매출액 : "))
success = 0
total = 0
max =0
maxday=""
minday=""
for i in ["월","화","수","목","금","토","일"]:
    money = int(input(f"{i}요일 매출 : "))
    total += money
    if money>max:
        max=money
        maxday=i
        if i=="월":
            min=max
            minday=i
    if min>money:
        min=money
        minday=i
    if money>target:
        print("-> 목표 달성")
        success += 1
    elif target*0.7<= money:
        print("-> 분발 필요")
    else :
        print("-> 목표 미달")

print(f"총 매출 : {total}원 | 일평균 : {(total/7):.0f}원")
print(f"최고 매출: {maxday} {max}원 | 최저 매출 {minday} {min}원")
print(f"목표 달성 : {success}일")