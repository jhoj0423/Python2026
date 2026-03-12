nums = [15, 3, 24, 8, 42, 10]

def find_min_max(list):
    max =0
    for li in list :
        if li> max :
            max = li
    min = max
    for li in list :
        if min>li :
            min = li
    return (max,min)

Max,Min = find_min_max(nums)

print(f"최대값 : {Max}, 최솟값 : {Min}")