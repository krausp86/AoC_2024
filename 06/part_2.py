# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 06.12.2024

import copy
import csv

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
        path_doc = 'guard_path_test.csv'
    else:
        input_doc = 'quiz_input_01.txt'
        path_doc = 'guard_path.csv'

    terrain = []
    position = (0, 0, 0) # x, y, dir
    with open(input_doc, 'r') as file:
        for lind, line in enumerate(file):
            terrain.append(list(line.strip()))
            if '^' in line:
                position = [lind, line.index('^'), 0]
    with open(path_doc, 'r') as file:
        reader = csv.reader(file)
        path = set(tuple(map(int, row[:2])) for row in reader)

    loops = 0
    original_position = copy.deepcopy(position)
    for bind, boulder_position in enumerate(path):
        linenum = boulder_position[0]
        charnum = boulder_position[1]
        print(f'Checking position {bind}/{len(path)} - ({linenum}|{charnum})')
        if terrain[linenum][charnum] != '#' and [linenum, charnum, 0] != original_position:
            terrcopy = copy.deepcopy(terrain)
            terrcopy[linenum][charnum] = '#'
            poscopy = copy.deepcopy(position)
            if is_loop(poscopy, terrcopy):
                loops += 1
                print(f'found loop at {linenum}/{charnum}')
    return loops

def is_loop(position, terrain):
    OOB = False
    visited_positions = []
    while not OOB:
        visited_positions.append(copy.deepcopy(position))
        if position[2] == 0:
            new_position = [position[0]-1, position[1], position[2]]
        elif position[2] == 1:
            new_position = [position[0], position[1]+1, position[2]]
        elif position[2] == 2:
            new_position = [position[0]+1, position[1], position[2]]
        elif position[2] == 3:
            new_position = [position[0], position[1]-1, position[2]]
        if is_out_of_bounds(new_position, terrain):
            return False
        if terrain[new_position[0]][new_position[1]] == '#':
            position[2] = (position[2] + 1) % 4
            continue
        position = new_position
        if position in visited_positions:
            return True
    return False

def is_out_of_bounds(position, terrain):
    if position[0] < 0 or position[0] >= len(terrain):
        return True
    if position[1] < 0 or position[1] >= len(terrain[0]):
        return True
    return False

def test_is_loop():
    input_doc = 'test_input_01.txt'

    terrain = []
    position = (0, 0, 0) # x, y, dir
    with open(input_doc, 'r') as file:
        for lind, line in enumerate(file):
            terrain.append(list(line.strip()))
            if '^' in line:
                position = [lind, line.index('^'), 0]

    linenum = 6
    charnum = 3
    terrcp = copy.deepcopy(terrain)
    poscp = copy.deepcopy(position)
    terrcp[linenum][charnum] = '#'
    assert is_loop(poscp, terrcp)

    linenum = 0
    charnum = 0
    terrcp = copy.deepcopy(terrain)
    poscp = copy.deepcopy(position)
    terrcp[linenum][charnum] = '#'
    assert not is_loop(poscp, terrcp)
    

def test_run_problem():
    assert run_problem(test=True) == 6 

if __name__ == '__main__':
    print(run_problem(test=False))

