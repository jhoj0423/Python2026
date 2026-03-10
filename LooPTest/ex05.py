#for 문으로 문제 풀이

count = int(input("측정 횟수"))
max =0

total =0

critical = 0

for i in range(1,count+1) :
    
    time = int(input(f"응답시간 {i} :"))

    total += time
    if max<time:
        max = time
        if i == 1:
            min = max

    if min>time:
        min = time 

    if time <= 100:
        print("FAST")
    elif time>=101 and time<=300:
        print("NORMAL")
    elif time>=301 and time<=1000:
        print("SLOW")
    elif time>=1001:
        print("CRITICAL")
        critical+=1
    
if critical/count>0.1:
    print("SLA 위반! 서버 점검이 필요합니다")
print(f"평균 응답시간 : {total}/{count}={(total/count):.1f}ms")
print(f"최대: {max}ms | 최소: {min}ms")