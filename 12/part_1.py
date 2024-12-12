# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 12.12.2024


def run_problem(test=False, testcase=0):
    if test:
        if testcase == 0:
            input_doc = 'test_input_01.txt'
        elif testcase == 1:
            input_doc = 'test_input_02.txt'
        elif testcase == 2:
            input_doc = 'test_input_03.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    topography = []

    with open(input_doc, 'r') as file:
        for line in file:
            topography.append(line[:-1])

    # Run through all positions, check if the current position is already in a 
    # known region
    regions = {}
    rid = 0
    for l_ind, line in enumerate(topography):
        for c_ind, char in enumerate(line):
            if any(t in value_list for value_list in regions.values()):
                print(f'({l_ind}/{c_ind}) - Position is already known')
            else:
                print(f'({l_ind}/{c_ind}) - New region found: {char}, Region ID {rid}')
    return 0

def test_problem():
    assert run_problem(test=True) == 140
    assert run_problem(test=True, testcase=1) == 772
    assert run_problem(test=True, testcase=2) == 1930
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(test=True))
