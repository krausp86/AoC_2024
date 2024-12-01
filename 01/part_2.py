# Advent of Code 2024 - Part 2
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

    ids = np.array(ids)
    first_ids = ids[:, 0]

    score = 0
    for id in first_ids:
        id_indices = np.where(ids[:, 1] == id)
        score += id * len(id_indices[0])

    return score

if __name__ == '__main__':
    print(run_problem(test=False))
