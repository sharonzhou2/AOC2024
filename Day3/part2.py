# INSTRUCTIONS

# 1. Read all from the input and match on the regex

# 2. Calculate all the regex for the dont's and minus it from all the current total.

# 3. Convert and remove the mul and format to int

# 4. Store the result

import re
from typing import List, Tuple

regex_exp = "mul\((\d{1,3}),(\d{1,3})\)"
negative_regex_exp = "don't\(\)(.*?)do\(\)|don't\(\)(.*)"

def read_input() -> List:
    normal_str = ""
    with open("input.txt") as file:
        normal_str = file.read()
    res = re.findall(negative_regex_exp, normal_str)
    negative_str = "".join([str(normal_text) for normal_text in re.findall(negative_regex_exp, normal_str)])
    
    matches = re.findall(regex_exp, normal_str)
    negative_matches = re.findall(regex_exp, negative_str)

    return matches, negative_matches
    

def calculate_number_matches(matches: Tuple[str, str], negative_matches: Tuple[str, str]) -> int:
    total = sum([int(x) * int(y) for x,y in matches])

    negative_total = sum([int(x) * int(y) for x,y in negative_matches])

    return total - negative_total



def main():
    matches, negative_matches = read_input()

    result = calculate_number_matches(matches, negative_matches)

    print(result)

if __name__ == "__main__":
    main()