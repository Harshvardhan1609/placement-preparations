res = [1,2,3,45]
start = 0
end = (len(res)-1)
while start<end:
    res[start] , res[end]  = res[end] , res[start]
    start = start + 1
    end = end -1
print(res)

