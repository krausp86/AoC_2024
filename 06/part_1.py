# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 06.12.2024

import csv

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    terrain = []
    direction = 0 # 0 - up, 1 - right - 2 - down - 3 - left
    position = (0, 0)
    visited_positions = []
    path_locations = []
    with open(input_doc, 'r') as file:
        for lind, line in enumerate(file):
            terrain.append(line.strip())
            if '^' in line:
                position = (lind, line.index('^'))
    OOB = False
    while not OOB:
        visited_positions.append(position)
        path_locations.append([position[0], position[1], direction])
        if direction == 0:
            new_position = (position[0]-1, position[1])
        elif direction == 1:
            new_position = (position[0], position[1]+1)
        elif direction == 2:
            new_position = (position[0]+1, position[1])
        elif direction == 3:
            new_position = (position[0], position[1]-1)
        if is_out_of_bounds(new_position, terrain):
            OOB = True
            break
        if terrain[new_position[0]][new_position[1]] == '#':
            direction = (direction + 1) % 4
        else:
            position = new_position
    with open('guard_path_test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(path_locations)
    return len(set(visited_positions))

def is_out_of_bounds(position, terrain):
    if position[0] < 0 or position[0] >= len(terrain):
        return True
    if position[1] < 0 or position[1] >= len(terrain[0]):
        return True
    return False

def test_run_problem():
    assert run_problem(test=True) == 41 

if __name__ == '__main__':
    print(run_problem(test=True))
