# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 03.12.2024

import re

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    summed_numbers = 0
    pattern = r'mul\((\d+),(\d+)\)'
    with open(input_doc, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            numbers = [(int(a), int(b)) for a, b in matches]
            mults = [x[0]*x[1] for x in numbers]
            summed_numbers += sum(mults)
    return summed_numbers


def test_run_problem():
    assert run_problem(test=True) == 161 

if __name__ == '__main__':
    print(run_problem(test=False))
