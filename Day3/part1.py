# 1. Read all from the input and match on the regex

# 2. Convert and remove the mul and format to int

# 3. Store the result

import re
from typing import List, Tuple

regex_exp = "mul\((\d{1,3}),(\d{1,3})\)"

def read_input() -> List[str]:
    matches = []
    with open("input.txt") as file:
        for rows in file.readlines():
            row_matches = re.findall(regex_exp, rows)
            matches.extend(row_matches)
    
    return matches

    

def calculate_number_matches(matches: Tuple[str, str]) -> int:

    total = 0

    for x, y in matches:
        total += int(x) * int(y)

    return total



def main():
    matches = read_input()

    result = calculate_number_matches(matches)

    print(result)

if __name__ == "__main__":
    main()