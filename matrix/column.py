# row  = int(input())
# column = int(input())
# result = []

# matrix  = [[None for i in range(column)] for j in range(row)]

# for i in range(row):
#     for j in range(column):
#         matrix[i][j] = int(input())

# for i in range(row):
#     for j in range (column):
#         result.append(matrix[j][i])
# print(matrix)
# print(result)



matrix = [[7,8,9],[10,11,12],[13, 15, 18]]
result = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        result.append(matrix[j][i])

print(result)
