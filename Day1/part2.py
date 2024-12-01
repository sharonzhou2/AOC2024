import sys
import collections

# 1. Read from the rows from the file and store that in an array of list 1 and list 2

# 2. Store each of the values in the list1 as a key in the dictionary mapped to an initial value of 0, ensure that list1 is a set, we cannot have duplicate keys

# 3. Iterate through each of the key value pairs and multiply it to retrieve the total similarity

# 4. Add the total and return the similarity

def read_from_input(list1, list2) -> None:

    with open("input.txt") as input_file:
        rows = input_file.readlines()
        for row in rows:
            [number1, number2] = row.split()
            list1.append(int(number1))
            list2.append(int(number2))



def calculate_similarity() -> int:

    list1 = []
    list2 = []

    total_similarity = 0

    read_from_input(list1, list2)

    list1 = set(list1)

    mapped_count = dict.fromkeys(list1, 0)

    for num in list2:
        if num in list1:
            mapped_count[num] += 1
    
    for val, multiplier in mapped_count.items():
        total_similarity += val * multiplier


    return total_similarity


def main() -> int:
    result = calculate_similarity()

    print(result)

    return result

if __name__ == '__main__':
    sys.exit(main())