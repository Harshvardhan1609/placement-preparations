arr = [1, 3, 4, 5, 7, 10, 11]
target = 9
result = []
hashmap = {}

for i in range(len(arr)):
    diff = target - arr[i]
    if diff in hashmap:
        result.append([hashmap[diff], i])
    hashmap[arr[i]] = i

# Sort the result to have pairs in ascending order
result.sort()

print(result)