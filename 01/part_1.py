# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 01.12.2024

import numpy as np

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    ids = []
    with open(input_doc, 'r') as file:
        for line in file:
            line_elements = [int(n) for n in line.split()]
            ids.append(line_elements)

    ids = np.sort(np.array(ids), axis=0)
    diff = np.abs(ids[:,0] - ids[:,1])
    return np.sum(diff)


if __name__ == '__main__':
    print(run_problem(test=False))
