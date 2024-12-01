import sys
import heapq

# 1. Read from the rows from the file and store that in an array of list 1 and list 2

# 2. Convert this to a min heap for both

# 3. Pop the first element of each of the min heap and calculate the distance

# 4. Add the distance to the running total

def read_from_input(list1, list2) -> None:

    with open("input.txt") as input_file:
        rows = input_file.readlines()
        for row in rows:
            [number1, number2] = row.split()
            list1.append(int(number1))
            list2.append(int(number2))



def calculate_distance() -> int:

    list1 = []
    list2 = []

    total_distance = 0

    read_from_input(list1, list2)

    heapq.heapify(list1)
    heapq.heapify(list2)

    while list1 or list2:
        dist1 = heapq.heappop(list1)
        dist2 = heapq.heappop(list2)

        total_distance += abs(dist1 - dist2)

    return total_distance


def main() -> int:
    result = calculate_distance()

    print(result)

    return result

if __name__ == '__main__':
    sys.exit(main())