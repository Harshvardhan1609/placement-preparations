arr = [1,0,2]
n = len(arr)

totalsum = n*(n+1)/2
sum = 0

for i in range(n):
    sum += arr[i]

a = totalsum-sum
print(a)