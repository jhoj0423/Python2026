member_data = [
{"name": "김철수", "age": 20},
{"name": "이영희", "age": 25},
{"name": "박민수", "age": 18}
]

overTwenties = []

for m in member_data :
    if m['age'] >= 20:
        overTwenties.append(m['name'])

print(overTwenties)