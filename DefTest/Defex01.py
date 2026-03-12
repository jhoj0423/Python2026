books = [("파이썬 기초", 15000), ("자바의 정석", 25000), ("React 입문", 18000)]

total = 0
print("---- 도서 목록 ----")
for b in books:
    print(f"도서명 : {b[0]} , 가격 : {b[1]}원")
    total += b[1]

print(f"\n전체 도서 합계 : {total} 원")