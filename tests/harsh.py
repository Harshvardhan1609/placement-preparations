n, k = map(int,input().split())
arrs = list(map(int,input().split()))

def rotate(L, start, end):
    k = L.index(start)
    L = L[k+1:]+L[0:k+1]
    return L

arrs  = rotate(arrs,k,len(arrs)-1)
result = " ".join([str(x) for x in arrs])
print(result)