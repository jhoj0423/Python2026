# 딕셔너리 = 오브젝트 이다.
# 딕셔너리 => key : value 가 쌍으로 존재한다.
# 딕셔너리 출력하는 방법
# 딕셔너리 dict['key']로 절대 dict.key 로 출력할 수 없다.
# phone_book = {'name':'홍길동','age':7,'class':'고급'}

phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
phone_book['고라니'] = '010-1234-5679'
phone_book['두뭉치'] = '010-1234-5670'

print(phone_book)

print(phone_book.keys())

print(phone_book.values())

# 문제) phone_book를 강감판 010-6543-3211 이런 형식으로 출력시키시오 단, for문 사용

for person in phone_book.keys():
    print(person,phone_book[person])
