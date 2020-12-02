import os

def read_input(input_file):
    input = open(os.path.dirname(__file__) + '/' + input_file, 'r')
    return input.readlines()

def part_1(input_lines):
    for line_outer in input_lines:
        line_outer_int = int(line_outer)
        for line_inner in input_lines:
            line_inner_int = int(line_inner)
            if line_outer_int + line_inner_int == 2020:
                return line_outer_int * line_inner_int

def part_2(input_lines):
    for line_outer in input_lines:
        line_outer_int = int(line_outer)
        for line_mid in input_lines:
            line_mid_int = int(line_mid)
            for line_inner in input_lines:
                line_inner_int = int(line_inner)
                if line_outer_int + line_mid_int + line_inner_int == 2020:
                    return line_outer_int * line_mid_int * line_inner_int

input_lines = read_input("input.txt")
print("Solution to part 1:", part_1(input_lines))
print("Solution to part 2:", part_2(input_lines))
