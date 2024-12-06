# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 05.12.2024 - Nachtrag 06.12.2024


def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    still_rules = True
    rules = []
    processes = []
    added_numbers = 0
    with open(input_doc, 'r') as file:
        for line in file:
            if line == '\n':
                still_rules = False
                continue
            if still_rules:
                numbers = tuple(map(int, line.split('|')))
                rules.append(numbers)
            else:
                processes.append(list(map(int, line.split(','))))
    
    # An dieser Stelle wurden die Regeln und die Prozesse eingelesen
    # Durchlaufe nun alle Prozesse und pruefe, ob die Regeln eingehalten werden
    for process in processes:
        if check_process(process, rules):
            added_numbers += process[int(len(process)/2)]

    return added_numbers

def check_process(process, rules):
    # Pruefe, ob die Regeln eingehalten werden
    for i, num in enumerate(process):
        for rule in rules:
            if num == rule[0]:
                # In diesem Fall darf die zweite Nummer nicht davor auftreten
                if rule[1] in process[:i]:
                    return False
            elif num == rule[1]:
                # In diesem Fall darf die erste Nummer nicht danach auftreten
                if rule[0] in process[i+1:]:
                    return False
            else:
                continue
    return True


def test_run_problem():
    assert run_problem(test=True) == 143 

if __name__ == '__main__':
    print(run_problem(test=False))
