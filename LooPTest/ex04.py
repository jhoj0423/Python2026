count = int(input("토큰 수를 입력하세요 : "))
num=0

normal =0
danger =0
for i in range(count):
    num+=1
    time=int(input(f"토큰 {num} 잔여시간 분 : "))
    if time<=0:
        print("[만료] 즉시 재발급 필요")
        danger += 1
    elif time>=1 and time<=10:
        print("[위험] 곧 만료됩니다. 갱신 권장")
        danger += 1
    elif time>=11 and time<=30:
        print("[주의] 만료가 가까워지고 있습니다.")
        danger += 1
    elif time>=31 :
        print("[정상] 유효한 토큰")
        normal += 1

print("---  요약  ---")
print(f"정상 토큰 : {normal}개 / 위험.만료 토큰 : {danger}개")