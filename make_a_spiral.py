from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'
    UP = 'up'


def get_next_direction(current_direction: Direction) -> Direction:
    directions = list(Direction)
    current_index = directions.index(current_direction)
    next_index = (current_index + 1) % len(directions)
    return directions[next_index]


def handle_direction(direction: Direction, row: int, col: int, length: int, spiral: List[List[int]]) -> Tuple[Direction, int, int, int, List[List[int]]]:
    if direction == Direction.RIGHT:
        while col + 1 != length and spiral[row][col + 1] != 0:
            spiral[row][col] = 0
            col += 1
        direction = get_next_direction(direction)
        col -= 1
    elif direction == Direction.DOWN:
        while row + 1 != length and spiral[row + 1][col] != 0:
            spiral[row][col] = 0
            row += 1
        direction = get_next_direction(direction)
        row -= 1
    elif direction == Direction.LEFT:
        while col != 0 and spiral[row][col - 1] != 0:
            spiral[row][col] = 0
            col -= 1
        direction = get_next_direction(direction)
        col += 1
    elif direction == Direction.UP:
        while row != length and spiral[row - 1][col] != 0:
            spiral[row][col] = 0
            row -= 1
        direction = get_next_direction(direction)
        row += 1

    return direction, row, col, length, spiral


def spiralize(size: int) -> List[List[int]]:
    spiral = [[1 for _ in range(size)] for _ in range(size)]
    length = len(spiral[0])

    row, col = 1, 0
    direction = Direction.RIGHT
    for _ in range(size):
        direction, row, col, length, spiral = handle_direction(direction, row, col, length, spiral)

    return spiral


def main():
    size = 7
    output = spiralize(size)
    for r in output:
        print(*r)


if __name__ == "__main__":
    main()
