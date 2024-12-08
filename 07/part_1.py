# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 07.12.2024

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    calibration_result = 0

    with open(input_doc, 'r') as file:
        for line in file:
            sep_1 = line.split(':')
            sep_2 = sep_1[1].strip().split(' ')
            if is_valid_calculation(int(sep_1[0]), tuple(map(int, sep_2))):
                calibration_result += int(sep_1[0])
            
    return calibration_result

def is_valid_calculation(solution, parameters):
    num_calc = len(parameters)-1
    operator_choices = [list(map(int, bin(i)[2:].zfill(num_calc))) for i in range(2**num_calc)]
    
    for operators in operator_choices:
        if run_calculation(parameters, operators) == solution:
            return True
    return False
    

def run_calculation(parameters, operators):
    solution = parameters[0]
    for o_ind, op in enumerate(operators):
        if op == 1:
            solution += parameters[o_ind+1]
        else:
            solution *= parameters[o_ind+1]
    return solution

def test_run_problem():
    assert run_problem(test=True) == 3749 

if __name__ == '__main__':
    print(run_problem(test=False))
