# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX

# XMAS 

# SAMX

# X
#   M
#     A
#       S

# X
#   M
#     A
#       S


# X
# M
# A
# S

# S
# A
# M
# X


# 1. Iterate through the string a a 2D row, and check every direction, left, right, down, up, left bottom diagonal and right bottom diagonal, left top diagonal, and right top diagonal

# 2. That makes 8 different directions required to check if th next letter exists

# 3. Account for corner cases, if the next letter is out of bounds or not part of the next letter, move on this does not count

# 4. Return the total found words for 'XMAS'

# 4. Since we are looking at this string O(N) * 8 this is big O(N) solution

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
        (1,0),
        (-1,0),
        (0,1),
        (0,-1),
        (-1, 1),
        (-1,-1),
        (1,1),
        (1,-1)
    ]

    skipped = set()

    WORD = "MAS"
    max_level = len(WORD)

    for level in range(1, max_level+1):
        for idx, (x, y) in enumerate(DIRECTIONS):
            _i = (level * x) + i
            _j = (level * y) + j
            if idx in skipped:
                continue
            if _i == ROWS or _i < 0 or _j == COLS or _j < 0 or input_matrix[_i][_j] != WORD[level - 1]:
                skipped.add(idx)
                continue
            
            if level == max_level:
                count_total += 1
    
    return count_total 
            
    

def calculate_counts(input_matrix: List[List[str]]) -> int:

    ROWS = len(input_matrix)
    COLS = len(input_matrix[0])

    total = 0

    for i in range(ROWS):
        for j in range(COLS):
            if input_matrix[i][j] == 'X':
                total += check_directions(input_matrix, ROWS, COLS, i, j)


    return total


def main():
    input_matrix = read_input()

    result = calculate_counts(input_matrix)

    print(result)


if __name__ == "__main__":
    main()