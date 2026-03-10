
# 문제) 1부터 50까지의 합을 구하기
# 단, while문 이용

result = 1
count = 1
""" while True:
    count = count + 1
    result = result+count
    if count == 50:
        break
print(result) """

# 다중 while문을 이용해서 구구단 2단부터 9단까지 출력

num=2
while True:
    count = 1
    print(f"{num}단")
    while count<=9:
        print(f"{num}X{count}={num*count}")
        count+=1
    num+=1
    if num == 10:
        break

