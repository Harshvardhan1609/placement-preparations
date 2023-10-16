arr = [-2,-3,4,1,-2,1,5,-3]
maxi = max(arr)
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        sum = 0
        for k in range(i,j):
            sum = sum + arr[k]
        maxi = max(sum , maxi)
print(maxi)