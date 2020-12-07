import os
import re

def read_input(input_file):
    input = open(os.path.dirname(__file__) + '/' + input_file, 'r')
    return input.readlines()

def part_1(input_lines):
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    count = 0
    parsed_passport = []

    current_line = 0
    while current_line <= len(input_lines):
        if current_line == len(input_lines) or len(input_lines[current_line]) == 1:
            # Evaluate last passport
            all_found = True
            for required_field in required_fields:
                found = False
                for field in parsed_passport:
                    if field[0:3] == required_field:
                        found = True
                        break
                if found == False:
                    all_found = False
                    break

            if all_found == True:
                count += 1

            # Clear last passport
            parsed_passport = []
            current_line += 1
            continue

        parsed_passport = parsed_passport + input_lines[current_line].split()
        current_line += 1

    return count

def part_2_validate_field(field):
    key = field.split(':')[0]
    value = field.split(':')[1]

    if key == 'byr':
        if value.isdigit() and int(value) >= 1920 and int(value) <= 2002:
            return True
    elif key == 'iyr':
        if value.isdigit() and int(value) >= 2010 and int(value) <= 2020:
            return True
    elif key == 'eyr':
        if value.isdigit() and int(value) >= 2020 and int(value) <= 2030:
            return True
    elif key == 'hgt':
        if (value[:-2].isdigit()
            and ((value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193)
            or (value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76))):
            return True
    elif key == 'hcl':
        if re.match('^#[0-9a-f]{6}$', value):
            return True
    elif key == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    elif key == 'pid':
        if re.match('^[0-9]{9}$', value):
            return True

    return False

def part_2(input_lines):
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    count = 0
    parsed_passport = []

    current_line = 0
    while current_line <= len(input_lines):
        if current_line == len(input_lines) or len(input_lines[current_line]) == 1:
            # Evaluate last passport
            all_found = True
            for required_field in required_fields:
                found = False
                for field in parsed_passport:
                    if field[0:3] == required_field:
                        found = part_2_validate_field(field)
                        break
                if found == False:
                    all_found = False
                    break

            if all_found == True:
                count += 1
                print(parsed_passport)

            # Clear last passport
            parsed_passport = []
            current_line += 1
            continue

        parsed_passport = parsed_passport + input_lines[current_line].split()
        current_line += 1

    return count

input_lines = read_input("input.txt")
print("Solution to part 1:", part_1(input_lines))
print("Solution to part 2:", part_2(input_lines))
