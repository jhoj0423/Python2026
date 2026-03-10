
# 다중 for문을 이용하여 구구단 2단~ 9단 출력

for i in range(2,10) :
    print(f"------{i}단 -----------")
    for j in range(1,10):
        print(f"{i}X{j}={i*j}")
    print()