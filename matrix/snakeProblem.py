matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = []
count = 1
for i in range(0,len(matrix)):
    if count == 1:
        for j in range(0,len(matrix)):
            result.append(matrix[i][j])
            count = 0
    else:
        for j in range(len(matrix),0,-1):
            result.append(matrix[i][j-1])
            count = 1
print(result)
final  = " ".join(str(x) for x in result)
print(final)

#[1, 2, 3, 6, 5, 4, 7, 8, 9]