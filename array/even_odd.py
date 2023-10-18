n = int(input())
res = []
sum = 0
for i in range(0,n):
    a = int(input())
    res.append(a)

for i in res:
    if i%2 == 0:
        print("even")
    else:
        print("odd")