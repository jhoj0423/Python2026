# info = ["name","email","age","grade"]

member = {
'name' : '김파이썬',
'email' : 'python@example.com',
'age' : 28,
'grade' : 'GOLD'
}

# member ={}
print("=== 회원 정보 ===")
#for memberinfo in info :
#    answer = input(f"{memberinfo} : ")
#    member[memberinfo] = answer

print(member)
print(member.keys())
if int(member['age'])<20 :
    print("연령 구간 : 주니어")
elif int(member['age'])>20 and  int(member['age'])<=39:
    print("연령 구간 : 일반")
else :
    print("연령 구간 : 시니어")

if 'phone' not in member.keys() :
    print("전화번호 : 미등록")
