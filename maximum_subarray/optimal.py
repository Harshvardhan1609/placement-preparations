arr = [-2,-2,4,-1,-2,1,5,-3]
maxss = min(arr)
sum = 0
for i in range(0,len(arr)):
    sum += arr[i]
    if sum < 0:
        sum = 0
    maxss = max(maxss,sum)
print(maxss)