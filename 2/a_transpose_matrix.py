rows_count = int(input())
columns_count = int(input())

matrix = []
for i in range(rows_count):
    matrix.append([int(x) for x in input().split()])


print(*matrix)