arr = [1, 3, 4, 5, 7, 10, 11]
target = 9
result = []
sum = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            result.extend([i,j])
print(result)
    
        