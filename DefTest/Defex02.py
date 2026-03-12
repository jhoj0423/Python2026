score = int(input("점수를 입력하세요 : "))

def get_grade(num):
    if num>= 90:
        print("학생의 학점은 A입니다")
    elif num >=80:
        print("학생의 학점은 B입니다")
    elif num >=70:
        print("학생의 학점은 C입니다")
    else:
        print("학생의 학점은 F입니다")

get_grade(score)
