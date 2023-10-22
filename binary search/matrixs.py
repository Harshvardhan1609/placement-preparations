a = [[0,0,1,1,1],[0,0,0,1,1],[0,1,1,1,1],[0,0,0,0,1]]
def BinarySearch(arr,low,high,target):
    while low <= high:
        mid = (low+high)//2
        if target <= arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return low

count = 0
globel = 0
index = 0
for i in range(0,len(a)):
    count = len(a[i])-BinarySearch(a[i],0,len(a[i])-1,1)
    if count > globel:
        globel = count
        index = i
    else:
        pass

print(index)


