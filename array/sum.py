n = int(input())
res = []
sum = 0
for i in range(0,n):
    a = int(input())
    res.append(a)

for i in res:
    sum = sum + i
print(sum)