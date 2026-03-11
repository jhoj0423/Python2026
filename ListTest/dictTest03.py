# 문제) 콜라:7 사이다:6 우유:8 커피:20
# 위 자료를 drink딕셔너리로 작성할 것
# 음료수 이름을 입력하세요 / 콜라 => 7

drink ={}
drink['콜라'] = 7
drink['사이다'] = 6
drink['우유'] = 8
drink['커피'] = 10

item = input("음료수 이름을 입력하세요 : ")
print(f"{item} => {drink[item]}")