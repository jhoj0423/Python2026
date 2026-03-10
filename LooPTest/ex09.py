msg = ["DB 마이그레이션 완료 여부","application-prod.properties 설정 확인","JWT Secret Key 변경 여부","CORS 허용 도메인 설정 완료","API 엔드포인트 테스트 통과"]
passmsg = [] 
for i in range(5):
    chk = input(f"[{i+1}/5] {msg[i]} (Y/N) : ").lower()
    if chk == "y":
        print("-> 완료")
    else:
        print("-> 미완료")
        passmsg.append(i)
if len(passmsg) == 0:
    print("배포 승인! 배포를 진행하세요")
else:
    print(f"배포 보류! {len(passmsg)}개 항목을 해결 후 재시도하세요")
    for j in range(len(passmsg)):
        print(f"[{passmsg[j]+1}] {msg[passmsg[j]]}")