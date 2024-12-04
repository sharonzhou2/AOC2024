# M   S
#   A
# M   S


# M   M
#   A
# S   S

# S   M
#   A
# S   M

# S   S
#   A
# M   M


# 1. Iterate through the string a a 2D row, and when we stumble on an 'A' character check the left bottom diagonal and right bottom diagonal, left top diagonal, and right top diagonal

# 2. That makes 4 different directions required to check if th next letter exists

# 3. Account for corner cases, if the next letter is out of bounds or not part of the next letter, move on this does not count

# 4. Return the total found words for 'MAS'

# 5. Since we are looking at this string O(N) * 4 this is big O(N) solution

# 6. Iterate through directions, if it is not M or S in the corner, continue, if it is a M the bottom ahs to be an S, vice versa

from typing import List


def read_input() -> List[List[str]]:

    input_matrix = []

    with open("input.txt") as file:
        for line in file.readlines():
            input_matrix.append([letter for letter in line if letter != '\n'])


    return input_matrix


def check_directions(input_matrix: List[List[str]], ROWS: int, COLS:int, i: int, j: int) -> int:

    count_total = 0
    DIRECTIONS = [
        [(-1, 1), (1, -1)],
        [(-1,-1), (1,1)],
    ]

    for (before_row, after_row) in DIRECTIONS:
        
        _i = before_row[0] + i
        _j = before_row[1] + j

        _l = after_row[0] + i
        _m = after_row[1] + j

        if _i == ROWS or _i < 0 or _j == COLS or _j < 0 or _l == ROWS or _l < 0 or _m == COLS or _m < 0:
            break

        if input_matrix[_i][_j] == 'M' and input_matrix[_l][_m] == 'S' or input_matrix[_i][_j] == 'S' and input_matrix[_l][_m] == 'M':
            count_total += 1
    
    return 1 if count_total == 2 else 0
            
    

def calculate_counts(input_matrix: List[List[str]]) -> int:

    ROWS = len(input_matrix)
    COLS = len(input_matrix[0])

    total = 0

    for i in range(ROWS):
        for j in range(COLS):
            if input_matrix[i][j] == 'A':
                total += check_directions(input_matrix, ROWS, COLS, i, j)


    return total


def main():
    input_matrix = read_input()

    result = calculate_counts(input_matrix)

    print(result)


if __name__ == "__main__":
    main()