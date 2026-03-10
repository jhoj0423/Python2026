response = int(input("상태코드를 입력하세요 : "))
if response == 200:
    print(f"{response}OK-요청성공")
elif response == 201:
    print(f"{response}Created - 리소스 생성 성공")
elif response == 400:
    print(f"{response}Bad Request - 잘못된 요청")
elif response == 401:
    print(f"{response}Unauthorized - 인증 필요")
elif response == 403:
    print(f"{response}Forbidden - 접근 권한 없음")
elif response == 404:
    print(f"{response}Not Found - 리소스 없음")
elif response == 500:
    print(f"{response}Internal Server Error - 서버 내부 오류")
else :
    print("Unknown Status Code")

# 200부터 299까지
if response >=200 and response<=299:
    print("2xx - 성공")
# 400부터 499까지
elif response >=400 and response<=499:
    print("4xx - 클라이언트 오류")
# 500부터 599까지
elif response >=500 and response<=599:
    print("5xx - 서버 오류")
else :
    print("알수 없음")