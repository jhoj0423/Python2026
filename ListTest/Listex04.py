response = {
'code' : 200,
'message': 'success',
'data' : [
        {'userId': 'user01', 'name': '이자바', 'score': 95},
        {'userId': 'user02', 'name': '박리액트', 'score': 82},
        {'userId': 'user03', 'name': '최스프링', 'score': 91},
        {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
    ]
}

print("=== 전체 성적 ===")
goodkid =[]
for i in response['data']:
    print(f"{i['name']} {i['userId']} {i['score']}점")
    if i['score']>90 :
        goodkid.append(i)

print(f"\n=== 우수 수장생 (90점 이상): {len(goodkid)}명")
for list in goodkid:
    print(f"★ {list['name']} : {list['score']}점")
