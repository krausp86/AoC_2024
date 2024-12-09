# Advent of Code 2024 - Part 2
# Patrick Kraus-Füreder
# 08.12.2024

from itertools import combinations

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    Antennas = {}
    Nodes = []
    Field_size = [0, 0]

    with open(input_doc, 'r') as file:
        for linenum, line in enumerate(file):
            Field_size[0] += 1
            if linenum==0:
                Field_size[1] = len(line[:-1])
            found_chars = [(i, char) for i, char in enumerate(line[:-1]) if char != '.']

            for char in found_chars:
                if char[1] not in Antennas.keys():
                    Antennas[char[1]] = [(linenum, char[0])]
                else:
                    Antennas[char[1]].append((linenum, char[0]))

    for antenna_type in Antennas.keys():
        for combo in combinations(Antennas[antenna_type], 2):
            dA = vector_subtract(combo[0], combo[1])
            Nodes.append(combo[0])
            Nodes.append(combo[1])
            nOOB = True
            n = 0
            while nOOB:
                n +=1
                AP = vector_add(combo[0], vector_multiply(dA, n))
                if is_within_bounds(AP, Field_size):
                    Nodes.append(AP)
                else:
                    nOOB = False
            nOOB = True
            n = 0
            while nOOB:
                n +=1
                AM = vector_subtract(combo[1], vector_multiply(dA, n))
                if is_within_bounds(AM, Field_size):
                    Nodes.append(AM)
                else:
                    nOOB = False

    Nodes = set(Nodes)

    return len(Nodes)

def vector_subtract(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

def vector_add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

def vector_multiply(v, n):
    return (v[0]*n, v[1]*n)

def is_within_bounds(v, bounds):
    return v[0] >= 0 and v[0] < bounds[0] and v[1] >= 0 and v[1] < bounds[1]

def test_run_problem():
    assert run_problem(test=True) == 34 

if __name__ == '__main__':
    print(run_problem(test=False))
