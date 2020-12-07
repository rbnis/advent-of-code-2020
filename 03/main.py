import os

def read_input(input_file):
    input = open(os.path.dirname(__file__) + '/' + input_file, 'r')
    return input.readlines()

def part_1(input_lines):
    count = 0
    increment_h = 3
    increment_v = 1

    position_h = 0
    position_v = 0

    while position_v < len(input_lines):
        if input_lines[position_v][position_h] == "#":
            count += 1

        position_h += increment_h
        if position_h >= len(input_lines[position_v]) - 1:
            position_h = position_h - (len(input_lines[position_v]) - 1)
        position_v += increment_v

    return count

def part_2(input_lines):
    runs = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    value = 0
    for run in runs:
        count = 0
        increment_h = run[0]
        increment_v = run[1]

        position_h = 0
        position_v = 0

        while position_v < len(input_lines):
            if input_lines[position_v][position_h] == "#":
                count += 1

            position_h += increment_h
            if position_h >= len(input_lines[position_v]) - 1:
                position_h = position_h - (len(input_lines[position_v]) - 1)
            position_v += increment_v

        value = count if value == 0 else value * count

    return value

input_lines = read_input("input.txt")
print("Solution to part 1:", part_1(input_lines))
print("Solution to part 2:", part_2(input_lines))
