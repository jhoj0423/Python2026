orders = [
{'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
{'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
{'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
{'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
{'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'},
]

total =0

print("=== 결제 완료 주문 ===")
orderfilter = []
for o in range(len(orders)):
    if orders[o]['status'] == "PAID" :
        orderfilter.append(orders[o])


print(orderfilter)

for list in orderfilter :
    print(f"{list['id']} 번 주문 / 상품 {list['product']} / 금액 : {list['amount']:,}원")
    total += list['amount']


print(f"총 결제 금액 : {total:,}원")
