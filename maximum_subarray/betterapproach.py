arr = [-2,-3,4,1,-2,1,5,-3]
maxs = 0
for i in range(0,len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        maxs = max(sum , maxs)

print(maxs)