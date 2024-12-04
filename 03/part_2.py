# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 03.12.2024

import re

def run_problem(test=False):
    if test:
        input_doc = 'test_input_02.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    summed_numbers = 0
    total_line = ''
    with open(input_doc, 'r') as file:
        for line in file:
            total_line+=line
    dolines = total_line.split('do()')
    for doline in dolines:
        splitted_line = doline.split("don't()")
        summed_numbers += find_and_multiply(splitted_line[0])
    return summed_numbers

def find_and_multiply(line):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, line)
    numbers = [(int(a), int(b)) for a, b in matches]
    mults = [x[0]*x[1] for x in numbers]
    return sum(mults)

def test_run_problem():
    assert run_problem(test=True) == 48 

if __name__ == '__main__':
    print(run_problem(test=False))
