#optimal
arr = [1, 3, 4, 5, 7, 10, 11]
target = 9
result = []
l , r = 0 , len(arr) -1
while l<r:
    curSum = arr[l] + arr[r]
    if curSum > target:
        r-=1
    elif curSum < target:
        l+=1
    else:
        print([l+1,r+1])
        
