#tier = input("회원등급(END 종료) : ")
#money = int(input("구매금액 : "))
num = 0
total =0
sale_total =0
total_pay = 0
while True:
    tier = input("회원등급(END 종료) : ").lower()
    sale =0
    if tier == "vip":
        money = int(input("구매금액 : "))
        sale = (money*0.2)+10000
        if money<sale:
            print("결제 금액이 너무 적습니다")
            continue
        print(f"할인금액 : {sale:.0f}원 -> 결제금액 : {money-sale:.0f}원")
        
    elif tier == "gold":
        money = int(input("구매금액 : "))
        sale = (money*0.1)+5000
        if money<sale:
            print("결제 금액이 너무 적습니다")
            continue
        print(f"할인금액 : {sale:.0f}원 -> 결제금액 : {money-sale:.0f}원")
    elif tier == "silver":
        money = int(input("구매금액 : "))
        sale = (money*0.05)
        print(f"할인금액 : {sale:.0f}원 -> 결제금액 : {money-sale:.0f}원")
    elif tier == "bronze":
        money = int(input("구매금액 : "))
        print(f"할인금액 : 0원 -> 결제금액 : {money:.0f}원")
    elif tier == "end":
        break
    else :
        print("등록되지 않은 등급입니다.")
    num+=1
    total += money
    sale_total +=sale
    total_pay += money-sale
print("--- 전체 주문 요약 ---")
print(f"주문 건수 : {num}")
print(f"총 구매금액 : {total}원 | 총 할인 : {sale_total:.0f}원 | 총 결제 : {total_pay:.0f}원")
