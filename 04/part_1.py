# Advent of Code 2024 - Part 1
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
            if char == 'X':
                print(f'Found X at {rind}, {cind}')
                # Suche nur nach Woertern, wenn es sich um ein X handelt
                if rind > 2 and cind >2:
                    if base_array[rind-1][cind-1] == 'M' and base_array[rind-2][cind-2] == 'A' and base_array[rind-3][cind-3] == 'S':
                        # Wort diagonal nach links oben gefunden
                        found_words += 1 
                        print(f'Found diagonal upper left at {rind}, {cind}')
                if rind >2:
                    if base_array[rind-1][cind] == 'M' and base_array[rind-2][cind] == 'A' and base_array[rind-3][cind] == 'S':
                        # Wort vertikal nach oben gefunden
                        found_words += 1
                        print(f'Found vertical up at {rind}, {cind}')
                if rind > 2 and cind < len(row)-3:
                    if base_array[rind-1][cind+1] == 'M' and base_array[rind-2][cind+2] == 'A' and base_array[rind-3][cind+3] == 'S':
                        # Wort diagonal nach rechts oben gefunden
                        found_words += 1
                        print(f'Found diagonal upper right at {rind}, {cind}')
                if cind > 2:
                    if base_array[rind][cind-1] == 'M' and base_array[rind][cind-2] == 'A' and base_array[rind][cind-3] == 'S':
                        # Wort horizontal nach links gefunden
                        found_words += 1
                        print(f'Found horizontal left at {rind}, {cind}')
                if cind < len(row)-3:
                    if base_array[rind][cind+1] == 'M' and base_array[rind][cind+2] == 'A' and base_array[rind][cind+3] == 'S':
                        # Wort horizontal nach rechts gefunden
                        found_words += 1
                        print(f'Found horizontal right at {rind}, {cind}')
                if rind < len(base_array)-3 and cind > 2:
                    if base_array[rind+1][cind-1] == 'M' and base_array[rind+2][cind-2] == 'A' and base_array[rind+3][cind-3] == 'S':
                        # Wort diagonal nach links unten gefunden
                        found_words += 1
                        print(f'Found diagonal lower left at {rind}, {cind}')
                if rind < len(base_array)-3:
                    if base_array[rind+1][cind] == 'M' and base_array[rind+2][cind] == 'A' and base_array[rind+3][cind] == 'S':
                        # Wort vertikal nach unten gefunden
                        found_words += 1
                        print(f'Found vertical down at {rind}, {cind}')
                if rind < len(base_array)-3 and cind < len(row)-3:
                    if base_array[rind+1][cind+1] == 'M' and base_array[rind+2][cind+2] == 'A' and base_array[rind+3][cind+3] == 'S':
                        # Wort diagonal nach rechts unten gefunden
                        found_words += 1
                        print(f'Found diagonal lower right at {rind}, {cind}')

    return found_words



def test_run_problem():
    assert run_problem(test=True) == 18 

if __name__ == '__main__':
    print(run_problem(test=False))
