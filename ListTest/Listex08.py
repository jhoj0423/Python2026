subjects = [
    {'subject':'Python 프로그래밍','score':92,'credit':3},
    {'subject':'SpringBoot 개발\t','score':88,'credit':3},
    {'subject':'React 프론트엔드','score':76,'credit':2},
    {'subject':'데이터베이스\t','score':95,'credit':3},
    {'subject':'알고리즘\t','score':68,'credit':2}
    ]
total =0
creditcount =0
print("===== 성적표 =====")
print("과목\t\t\t점수\t학점\t학점포인트\t이수학점")
print("-----------------------------------------------------------")
for list in subjects :
    if list['score']>=95:
        unit = 'A+'
        point = 4.5
    elif list['score']<95 and list['score']>=90:
        unit = 'A'
        point = 4.0
    elif list['score']<90 and list['score']>=85:
        unit = 'B+'
        point = 3.5
    elif list['score']<85 and list['score']>=80:
        unit = 'B'
        point = 3.0
    elif list['score']<80 and list['score']>=75:
        unit = 'C+'
        point = 2.5
    elif list['score']<75 and list['score']>=70:
        unit = 'C'
        point = 2.0
    elif list['score']<70 and list['score']>=60:
        unit = 'D'
        point = 1.0
    else:
        unit = 'F'
        point = 0
    list['unit'] = unit
    list['point'] = point
    total+=point*list['credit']
    creditcount+=list['credit']
    print(f"{list['subject']}\t{list['score']}점\t{list['unit']}\t{list['point']}\t\t{list['credit']}학점")

print(f"\nGPA :  {(total)/creditcount:.2f}/ 4.50 (총 {creditcount}학점)")
distribution={}
for i in range(len(subjects)):
    
    if subjects[i]['unit'] in distribution:
        distribution[subjects[i]['unit']]+= 1
    else:
        distribution[subjects[i]['unit']]=1


print(f"\n학점 분포 : {distribution}")