arrs = [0,0,1,1,0,1,0]
f = 0
e = 0
while e<len(arrs):
    if arrs[e] == 0:
        arrs[f], arrs[e] = arrs[e] , arrs[f]
        e+=1
        f+=1
    else:
        e+=1
print(arrs)
    