# list는 배열과 같은 역활을 한다
# list [숫자, 문자, 혼합] 사용가능
# 동적 => 고정길이가 아님
# 속도가 살짝 느림

heroes =[]
# 리스트 추가하는 방법
# append('추가할 문자 )=> 맨뒤에추가
# insert(인덱스 번호, '추가문가') => 인덱스 번호에 추가
heroes.append('아이언맨')
heroes.append('닥터 스트레인지')

heroes.insert(1,'퀵실버')
print(heroes)

#리스트 삭제 : remove('삭제할 문자')
#리스트 삭제 : del heroes[0] => 0번째 데이터 삭제
#리스트 삭제 : pop => 맨 마지막 데이터 삭제
heroes.remove('퀵실버')
print(heroes)
del heroes[1]
print(heroes)
heroes.pop()
print(heroes)
heroes.append('헐크')
heroes.append('로키')
heroes.append('토르')
heroes.append('그루트')
heroes.append('울버린')
heroes.append('데드풀')
print(heroes)

for hero in heroes:
    print(hero,end= " ")

# 리스트 슬라이스 하기
# heroes[0:3] => 0번재부터 3글자
# heroes[:3] => 처음부터 3글자
# heroes[3:] => 3번재부터 마지막글자 까지

cut = heroes[0:2]
print(cut)
cut = heroes[3:]
print(cut)

#문제 ) moivetitle = [] 에 아래 여화 제목 4개를 추가하시오
# 아이언맨, 토르, 헐크, 스칼렛 위치
moivetitle = []
moivetitle.append('아이언맨')
moivetitle.append('토르')
moivetitle.append('헐크')
moivetitle.append('스칼렛 위치')
print('---------moivetitle---------')


for m in moivetitle:
    print(m,end=" ")
print()
#문제 ) moivetitle = [] 에 토르가 존재하면 삭제하고 출력
if '토르' in moivetitle:
    moivetitle.remove('토르')
moivetitle.sort()    
for m in moivetitle:
    print(m,end=" ")