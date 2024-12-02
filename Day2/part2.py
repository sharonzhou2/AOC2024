
# 1. Read from the input of each row

# 2. A greedy solution should work as you want to optimize for the first value that causes it to be a 'bad' level

# 3. Re-calculate the row once the first value is removed


from typing import List


def read_from_input() -> List[int]:
    input = []
    with open("input.txt") as rows:
        for row in rows.readlines():
            input.append([int(num) for num in row.split()])
    return input

def check_safe_report(row: List[int]) -> bool:
    if len(row) < 2:
        raise Exception("Not a valid report row") 
    
    is_increasing = True
    has_removed = False
    curr_idx = 1
    prev, curr = row[curr_idx - 1], row[curr_idx]
    if curr < prev:
        is_increasing = False

    while curr_idx < len(row):
        prev, curr = row[curr_idx - 1], row[curr_idx]

        distance = curr - prev if is_increasing else prev - curr

        if distance < 1 or distance > 3:
            if has_removed:
                return False
            
            row.remove(prev)
            has_removed = True
            continue
        
        curr_idx += 1


    return True

def calculate_safe_reports() -> int:
    total_safe_reports = 0
    
    input = read_from_input()

    for row in input:
        if check_safe_report(row):
            total_safe_reports += 1

    return total_safe_reports

def main():
    result = calculate_safe_reports()

    print(result)

if __name__ == '__main__':
    main()