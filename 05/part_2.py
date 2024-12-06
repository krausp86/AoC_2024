# Advent of Code 2024 - Part 2
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
        if not check_process(process, rules):
            new_process = sort_by_rules(process, rules)
            added_numbers += new_process[int(len(new_process)/2)]

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

def sort_by_rules(process, rules):
    sorted = False
    while not sorted:
        for i, num in enumerate(process):
            for rule in rules:
                if num == rule[0]:
                    if rule[1] in process[:i]:
                        index_0 = process.index(rule[0])
                        index_1 = process.index(rule[1])
                        process[index_0], process[index_1] = process[index_1], process[index_0]
                elif num == rule[1]:
                    if rule[0] in process[i+1:]:
                        index_0 = process.index(rule[0])
                        index_1 = process.index(rule[1])
                        process[index_0], process[index_1] = process[index_1], process[index_0]
                else:
                    continue
        sorted = check_process(process, rules)
    return process

def test_run_problem():
    assert run_problem(test=True) == 123 

if __name__ == '__main__':
    print(run_problem(test=False))
