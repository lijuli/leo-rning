# Count matrix neighbours except diagonal elements.

# 4   -->  rows count
# 3   -->  columns count
# 1 2 3
# 0 2 6
# 7 4 1
# 2 7 0
# 3  --> coordinate
# 0  --> coordinate

# >> 7 7


rows_count = int(input())
columns_count = int(input())

matrix = []
for i in range(rows_count):
    matrix.append([int(x) for x in input().split()])

point_x = int(input())
point_y = int(input())

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
result = []

for direction in directions:
    x = point_x + direction[0]
    y = point_y + direction[1]

    if 0 <= x < rows_count and 0 <= y < columns_count:
        result.append(matrix[x][y])
result.sort()
print(result)
