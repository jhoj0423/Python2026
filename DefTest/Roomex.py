
# 방정보
rooms = [
    {'id': 101, 'roomname': '스탠다드 A', 'price': 100000, 'max': 2, 'status':True},
    {'id': 102, 'roomname': '스탠다드 B', 'price': 110000, 'max': 2, 'status':True},
    {'id': 201, 'roomname': '디럭스 룸', 'price': 250000, 'max': 4, 'status':True},
    {'id': 301, 'roomname': '스튀트 룸', 'price': 500000, 'max': 6, 'status':True}
]

#전체 방 정보 출력
def show_rooms():
    print("ID\t객실명\t\t가격\t\t최대인원\t상태")
    print("-------------------------------------------------")
    for r in rooms:
        if r['status'] == True:
            ment = "예약가능"
        else:
            ment = "예약 불가능"

        print(f"{r['id']}\t{r['roomname']}\t{r['price']:,}\t\t{r['max']}\t\t{ment}")

#예약하기

reservationList = []
def make_reservation(id,user,num):
    for r in rooms:
        if r['id'] == id:
            r['user'] = user
            r['num'] = num
            r['status'] = False
            reservationList.append(r)
    print(f"\n[성공] {user}님, {id}호 예약이 완료되었습니다")

#예약 내역 출력
def show_reservation():
    if reservationList == [] :
        print("아직 예약된 정보가 없습니다")
    for li in reservationList:
        print(f"성함 : {li['user']} | 객실번호 : {li['id']}호 | 인원 : {li['num']}")

#전체 매출 계산
total =0

def calculate_price():
    if reservationList != [] :
        for re in  reservationList:
            global total 
            if re['max'] >= re['num']:
                total+= re['price']*re['num']
            else :
                total += (re['price']*re['num']) + ((re['num']-re['max'])*20000) 
        print(f"\n현재 확정 매출 합계 : {total:,}원")


#예약 취소
def del_reservation(id,user):
    chking = True
    for re in reservationList:
        if re['id'] == id and re['user'] == user:
            reservationList.remove(re)
            chking == True
            break
        else:
            chking == False
    if chking == False:
        print("입력하신 정보에 해당하는 예약 정보가 존재하지 않습니다")



#반복문
while True :
    print("---- 리조트 예약 관리 시스템 ----")
    print("1. 객실 현황 보기")
    print("2. 객실 예약하기")
    print("3. 예약 내역 및 매출 확인")
    print("4. 프로그램 종료")
    print("5. 예약 취소하기")
    result = int(input("\n원하는 메뉴 번호를 선택하세요 : "))
    print("\n===================================\n")
    if result == 1:
        show_rooms()
    elif result == 2:
        show_rooms()
        print()
        roomId = int(input("예약할 객실 ID를 입력하세요 : "))
        maxCustomer = 0
        chk = True
        chk2 = True
        for r in rooms:
            if r['id'] == roomId and r['status'] == False :
                chk = False
                break
            if r['id'] == roomId :
                maxCustomer = r['max']
                chk2 = True
                chk = True
                break
            else:
                chk2 = False
        
        if chk == False:
            print("이미예약이 완료된 객실입니다")
            continue
        if chk2 == False:
            print("현재 선택하신 객실이 존재하지 않습니다")
            continue
        customer = input("예약자 성함을 입력하세요 : ")
        count = int(input(f"투숙 인원을 입력하세요 (최대 {maxCustomer}명) : "))
        if count > maxCustomer :
            print("최대인원보다 많은 인원을 선택하였습니다. 추가 지출이 발생할 수 있습니다 그대로 진행 하시겠습니까?")
            answer = input("y / n  : ")
            if answer == 'n':
                continue
        make_reservation(roomId,customer,count)
    elif result == 3:
        show_reservation()
        calculate_price()
    elif result == 4:
        print("포로그램을 종료합니다. 수고하셨습니다.")
        break
    elif result == 5:
        findrooms = input("예약 취소하고자하는 방의 ID를 적어주세요")
        finduser = input("예약 취소하고자하는 고객님의 성함을 작성해주세요")
        del_reservation(int(findrooms),finduser)
        
    else:
        print("1~4 번 메뉴중에서 선택해 주세요")

    print("\n===================================\n")