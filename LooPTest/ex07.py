pw = input("비밀번호 입력 : ")
num =0
if len(pw)>=8:
    print("[O] 길이 8자 포함")
    num+=1
else:
    print("[X] 길이 8자 포함")
chk1 = False
chk2 = False
chk3 = False
chk4 = False
for ch in pw :
    if (ch>= 'A' and ch <= 'Z'):
        chk1 = True
    if (ch>= 'a' and ch <= 'z'):
        chk2 = True
    if (ch>= '0' and ch <= '9'):
        chk3 = True
    if not(ch>= 'A' and ch <= 'Z') and not(ch>= 'a' and ch <= 'z') and not(ch>= '0' and ch <= '9') :
        chk4 = True

if chk1 == True:
    print("[O] 대문자 포함")
    num+=1
else:
    print("[X] 대문자 포함")

    
if chk2 == True:
    print("[O] 소문자 포함")
    num+=1
else:
    print("[X] 소문자 포함")

if chk3 == True:
    print("[O] 숫자 포함")
    num+=1
else:
    print("[X] 숫자 포함")
    
if chk4 == True:
    print("[O] 특수문자 포함")
    num+=1
else:
    print("[X] 특수문자 포함")

if num == 0:
    print("비밀번호 강도 : 취약 X")
elif num ==1:
    print("비밀번호 강도 : 매우약함")
elif num ==2:
    print("비밀번호 강도 : 약함")
elif num ==3:
    print("비밀번호 강도 : 중간")
elif num ==4:
    print("비밀번호 강도 : 강함")
elif num ==5:
    print("비밀번호 강도 : 매우 강함")



        
