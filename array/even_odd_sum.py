n = int(input())
res = []
even_sum = 0
odd_sum = 0
for i in range(0,n):
    a = int(input())
    res.append(a)

for i in res:
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(even_sum)
print(odd_sum)