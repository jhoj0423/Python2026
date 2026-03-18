from datetime import datetime,timedelta

# 기준 날짜 (연체 확인용)
today = '2025-06-10'

# 도서 목록
books = [
    {'id':'B001','title':'파이썬 완전정복','author':'홍길동\t','genre':'IT','total':3,'available':2},
    {'id':'B002','title':'데이터분석 입문','author':'김데이터','genre':'IT','total':2,'available':2},
    {'id':'B003','title':'알고리즘의 이해','author':'이알고\t','genre':'IT','total':2,'available':1},
    {'id':'B004','title':'채식주의자','author':'한강\t','genre':'소설','total':4,'available':4},
    {'id':'B005','title':'82년생 김지영','author':'조남주\t','genre':'소설','total':3,'available':3},
]


# 대출 기록
loans = [
    {'loan_id':'L001','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
    {'loan_id':'L002','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]


#도서목록 조회 함수
def show_books():
    print("도서ID\t제목\t\t저자\t\t장르\t전체\t가능\t상태")
    print("-------------------------------------------------------------------------")
    for  b in books:
        state = "대출가능"
        if b['available'] == 0: # 현재 대여가능한 도서가 없을때
            state = "대출불가"
        print(f"{b['id']}\t{b['title']}\t{b['author']}\t{b['genre']}\t{b['total']}\t{b['available']}\t{state}\t")


#도서 대출 함수
def loan_book(id,user):
    name = ""
    for b in books:
        if b['id'] == id:
            b['available'] -= 1
            name = b['title']
    date = datetime.strptime(today,'%Y-%m-%d')
    after_date = date+timedelta(days=14)
    af_date = f"{after_date:%Y-%m-%d}"
    num = len(loans)+1
    loanNum = "L"+f"{num:03d}" #대출번호는 L + (대출기록 목록개수 +1)
    loansLog = {'loan_id':f"{loanNum}",'member':f"{user}",'book_id':f"{id}",'loan_date':f"{today}",'due_date':af_date,'returned':False}
    loans.append(loansLog)
    
    print(f"[대출 완료] {user} 님이 '{name}' 을(를) 대출하였습니다.")
    print(f"대출번호 : {loanNum} | 반납예정일 : {af_date}")


#도서 반납 함수
def return_book(id):
    name = ""
    L_id = ""
    for l in loans:
        if l['loan_id'] == id:
            l['returned'] = True
            L_id =l['book_id']
    for b in books:
        if L_id == b['id']:
            name = b['title']
            b['available']+=1   
    print(f"[반납 완료] '{name}' 이(가) 반납되었습니다.")

#도서 대출 현황 조회 함수
def show_loans():
    
    print("\n대출번호 회원명\t도서제목\t\t대출일\t\t반납예정일\t반납여부")
    print("------------------------------------------------------------------------------")
    for l in loans:
        ment = "대출중"
        name =""
        if l['returned'] == True:
            ment = "반납완료"
        for b in books:
            if l['book_id'] == b['id']:
                name = b['title']
        print(f"{l['loan_id']}\t {l['member']}\t{name}\t\t{l['loan_date']}\t{l['due_date']}\t{ment}")
    print()
# 연체 현황 조회 함수
def show_overdue():
    print(f"\n=== 연체 현황 (기준일 : {today}) ===")
    print(f"\n대출번호  회원명 \t도서제목\t\t반납예정일")
    print("---------------------------------------------------")

    for l in loans:
        name = ""
        for b in books:
            if l['book_id'] == b['id']:
                name = b['title']
        
        date_obj = datetime.strptime(l['due_date'],'%Y-%m-%d')
        date = datetime.strptime(today,'%Y-%m-%d')
        if date > date_obj and l['returned'] == False:
            print(f"{l['loan_id']}\t  {l['member']}\t{name}\t\t{l['due_date']}")
    print()

#장르별 통계
def show_genre_stats():
    print("\n장르\t전체권수\t대출중")
    print("-----------------------------------------")
    IT_count =0
    IT_available =0
    novel_count =0
    novel_available =0
    for b in books:
        
        if b['genre'] == "IT":
            IT_count+=b['total']
            IT_available+=b['available']
        else:
            novel_count+=b['total']
            novel_available+=b['available']
    print(f"IT\t{IT_count}\t\t{IT_count-IT_available}")
    print(f"소설\t{novel_count}\t\t{novel_count-novel_available}")
# 반복문

while True:
    print("=== 도서관 대출 관리 시스템 ===\n")
    print("1. 도서 목록 조회")
    print("2. 도서 대출")
    print("3. 도서 반납")
    print("4. 대출 현황 조회")
    print("5. 연체 현황 조회")
    print("6. 장르별 통계")
    print("0. 종료")
    
    menuNum = int(input("메뉴를 선택해 주세요. : "))

    if menuNum == 1 :
        show_books()
    elif menuNum == 2 :
        userName = input("회원명을 입력하세요 : ")
        book_choice = input("대출할 도서ID를 입력하세요 : ")
        chk = True
        chk2 = True

        for b in books:
            if book_choice in b['id']:
                chk = True
                break
            else:
                chk = False
        if chk == False :
            print("\n등록되지 않은 도서 입니다.\n")
            continue
        for b in books :
            if b['id'] == book_choice and b['available'] == 0 :
                chk2 = False
        if chk2 == False :
            print('\n현재 대출 가능한 도서가 없습니다.\n')
            continue
        loan_book(book_choice,userName)
    elif menuNum == 3 :
        L_num = input("대출번호를 입력하세요 : ")
        chk = True
        chk2 = True
        for l in loans:
            if l['loan_id'] == L_num:
                chk = True
                break
            else:
                chk = False
        for l in loans:
            if l['returned'] == True and l['loan_id'] == L_num:
                chk2 = True
                break
            else:
                chk2 = False
        if chk == False:
            print("\n해당 대출 기록이 없습니다.\n")
            continue
        if chk2 == False:
            print("\n이미 반납된 도서입니다\n")
        return_book(L_num)
    elif menuNum == 4 :
        show_loans()
    elif menuNum == 5 :
        show_overdue()
    elif menuNum == 6 :
        show_genre_stats()
    elif menuNum == 0 :
        print("\n시스템을 종료합니다.\n")
        break
    else:
        print("\n선택하신 메뉴는 존재하지 않습니다\n")