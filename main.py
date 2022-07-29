grid = [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
        ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.']]


print(grid)

'''
for i in range(9):
    for j in range(6):
        print(grid[j][i], end='')
'''


# print original graph
for i in range(6):
    for j in range(9):
        print(grid[i][j], end='')
    print()


print('\n')
# Transpose
for j in range(9):
    for i in range(6):
        print(grid[i][j], end='')
    print()

