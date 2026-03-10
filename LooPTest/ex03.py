select =0
insert =0
update =0
delete =0
count =0

while True:
    anwser = input("쿼리 유형 입력 : ").upper() #무조건 소문자 upper 무조건 대문자 출력
    if anwser == "SELECT" :
        select += 1
        count +=1
    elif anwser == "INSERT":
        insert += 1
        count +=1
    elif anwser == "UPDATE":
        update += 1
        count +=1
    elif anwser == "DELETE":
        delete += 1
        count +=1
    elif anwser == "REPORT":
        print("--- 쿼리 실행 현황 ---")
        print(f"SELECT : {select}회 \n INSERT : {insert}회 \n UPDATE : {update}회 \n DELETE : {delete}회 \n 총 실행 : {count}회")
        
    elif anwser == "EXIT":
        print("--- 쿼리 실행 현황 ---")
        print(f"SELECT : {select}회 \n INSERT : {insert}회 \n UPDATE : {update}회 \n DELETE : {delete}회 \n 총 실행 : {count}회")
        if select/count>=0.7 : # 굳이 정수가 아닌 소수여도 계산이 가능하다
            print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")
        break
    else :
        print("알 수 없는 쿼리 유형입니다.")
