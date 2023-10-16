arr = [-2,1,-3,4,1,2,1,-5,4]
maxss = min(arr)
sum = 0
ma = []
arr_start = -1
arr_end = -1
for i in range(0,len(arr)):
    if sum == 0 : start = i
    sum += arr[i]
    if sum < 0:
        sum = 0
        ma.clear()
    if sum > maxss:
        maxss = sum
        arr_start = start
        arr_end = i
for i in range(arr_start,arr_end+1):
    ma.append(arr[i])
print(ma)    