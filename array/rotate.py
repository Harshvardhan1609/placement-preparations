arrs = [1,2,3,4,5,6,7]
def reverse(arr,start,end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start +=1
        end-=1
    return arr

k = int(input())
arrs = reverse(arrs,0,len(arrs)-1)
arrs = reverse(arrs,0,k-1)
arrs = reverse(arrs,k,len(arrs)-1)
print(arrs)