# 3

# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
# Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
# Диагональные элементы соседними не считаются.


# 4   -->  количество строк
# 3   -->  количество столбцов
# 1 2 3
# 0 2 6
# 7 4 1
# 2 7 0
# 3  --> координатa
# 0  --> координатa

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



# def print_matrix(matrix, i, j):
#     if (
#         i != j and
#         i in range(rows_count) and
#         j in range(columns_count)
#     ):
#         return matrix[i][j]


# # breakpoint()
# print(f'i = {i}, y = {y}, matrix = {matrix[i][y]}')
# print('-------')
# result = []
# result.append(print_matrix(matrix, i-1, y))
# result.append(print_matrix(matrix, i, y-1))
# result.append(print_matrix(matrix, i, y+1))
# result.append(print_matrix(matrix, i+1, y))

# # print(sorted(result))
# print(result)