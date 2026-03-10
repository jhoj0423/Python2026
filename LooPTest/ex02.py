
while True:
    userid = input("아이디 입력 (4 ~ 12자) :")
    if len(userid) >= 4 and len(userid)<=12:
        while True:
            userpw = input("비밀번호 입력(8자 이상, 숫자 포함)")
            if len(userpw)>=8 and userpw:
                while True:
                    email = input("이메일 입력")
                    if email.find("@") != -1 and email.find(".com") != len(email)-4:
                        print("유효성 검사 통과! API 요청을 전송합니다.")
                        break
                    else:
                        print("올바른 이메일 형식이 아닙니다. 다시 입력하세요")
                break
            else:
                print("비밀번호는 8자 이상이여야 합니다. 다시 입력하세요")
        break # 조건을 만족하면 반복문 종료
    else:
        print("아이디는4자 이상12자 이하여야 합니다. 다시 입력하세요.")

        """ digit = False
        
        for ch in pw:
            if ch >= '0' and ch <= '9':
                digit = True # 숫자가 포함되어 있어서 boolean값 변경
                break # 숫자를 찾았기때문에 반복 종료
        #숫자가 하나도 없으면 다시 입력
        if not digit:
            print("비밀번호에 숫자가 포함되어야 합니다, 다시 입력하세요")
        #모든 조건 만족하면 반복문 종료
        break
    while True:
        email = input("이메일 입력:")
        #if @ in 변수 : @가 변수안에 포함되어 있나라는 의미
        if "@" in email:
            break
        print("올바른 이메일 형식이 아니야, 다시 입력해주세요")
    print("유효성 검사 통과! API 요청을 전송합니다.") """