transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]
dict ={}
print("=== 월별 매출 ===")

for i in transactions:
    if i[0] in dict:
        dict[i[0]] += i[1]
    else:
        dict[i[0]] = i[1]


max = 0
maxday = ""
min = -1
minday = ""
total = 0
for li in dict:
    print(f"{li} : {dict[li]:,}원")
    total += dict[li]
    if dict[li] > max:
        max = dict[li]
        maxday = li
    if min == -1:
        min = dict[li]
        minday = li
    elif min>dict[li]:
        min = dict[li]
        minday = li


print(f"최고 매출 월 : {maxday} ({max}원)")
print(f"최저 매출 월 : {minday} ({min}원)")
print(f"월 평균 매출 : {total/len(dict):,.0f}원")

print(dict)