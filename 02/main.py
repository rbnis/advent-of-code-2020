import os

def read_input(input_file):
    input = open(os.path.dirname(__file__) + '/' + input_file, 'r')
    return input.readlines()

def part_1(input_lines):
    count = 0

    for line in input_lines:
        tokens = line.split()
        char_min = int(tokens[0].split('-')[0])
        char_max = int(tokens[0].split('-')[1])
        char_count = int(tokens[2].count(tokens[1][0]))

        if char_count >= char_min and char_count <= char_max:
            count += 1

    return count

def part_2(input_lines):
    count = 0

    for line in input_lines:
        tokens = line.split()
        char_pos1 = int(tokens[0].split('-')[0]) - 1
        char_pos2 = int(tokens[0].split('-')[1]) - 1

        if (tokens[2][char_pos1] == tokens[1][0]) ^ (tokens[2][char_pos2] == tokens[1][0]):
            count += 1

    return count

input_lines = read_input("input.txt")
print("Solution to part 1:", part_1(input_lines))
print("Solution to part 2:", part_2(input_lines))
