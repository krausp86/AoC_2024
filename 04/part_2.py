# Advent of Code 2024 - Part 2
# Patrick Kraus-Füreder
# 04.12.2024 - Nachtrag 06.12.2024


def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    base_array = []
    found_words = 0
    with open(input_doc, 'r') as file:
        for line in file:
            charline = list(line[:-1])
            base_array.append(charline)
    # Gehe alle Zeilen durch
    for rind, row in enumerate(base_array):
        # Gehe alle Zeichen der Zeile durch
        for cind, char in enumerate(row):
            if char == 'A':
                # Suche nur nach Woertern, wenn es sich um ein X handelt
                diagonal_MS = 0
                if rind > 0 and cind > 0 and rind < len(base_array)-1 and cind < len(row)-1:
                    if base_array[rind-1][cind-1] == 'M' and base_array[rind+1][cind+1] == 'S':
                        diagonal_MS += 1
                    if base_array[rind-1][cind-1] == 'S' and base_array[rind+1][cind+1] == 'M':
                        diagonal_MS += 1
                    if base_array[rind-1][cind+1] == 'M' and base_array[rind+1][cind-1] == 'S':
                        diagonal_MS += 1
                    if base_array[rind-1][cind+1] == 'S' and base_array[rind+1][cind-1] == 'M':
                        diagonal_MS += 1
                    if diagonal_MS == 2:
                        found_words += 1
    return found_words

def test_run_problem():
    assert run_problem(test=True) == 9 

if __name__ == '__main__':
    print(run_problem(test=False))
