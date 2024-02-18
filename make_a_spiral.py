def get_next_direction_index(dir_index):
    if dir_index == 3:
        return 0
    else:
        return dir_index + 1


def spiralize(size):
    spiral = [[1 for _ in range(size)] for _ in range(size)]
    directions = ['right', 'down', 'left', 'up']
    length = len(spiral[0])

    row, col = 1, 0
    dir_index = 0
    direction = directions[dir_index]
    for i in range(size):
        if direction == 'right':
            while col + 1 != length and spiral[row][col + 1] != 0:
                spiral[row][col] = 0
                col += 1
            dir_index = get_next_direction_index(dir_index)
            direction = directions[dir_index]
            col -= 1
        elif direction == 'down':
            while row + 1 != length and spiral[row + 1][col] != 0:
                spiral[row][col] = 0
                row += 1
            dir_index = get_next_direction_index(dir_index)
            direction = directions[dir_index]
            row -= 1
        elif direction == 'left':
            while col != 0 and spiral[row][col - 1] != 0:
                spiral[row][col] = 0
                col -= 1
            dir_index = get_next_direction_index(dir_index)
            direction = directions[dir_index]
            col += 1
        elif direction == 'up':
            while row != length and spiral[row - 1][col] != 0:
                spiral[row][col] = 0
                row -= 1
            dir_index = get_next_direction_index(dir_index)
            direction = directions[dir_index]
            row += 1

    return spiral


size = 5
output = spiralize(size)
for r in output:
    print(*r)
