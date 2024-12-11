# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 09.12.2024


def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    input_line = ''

    with open(input_doc, 'r') as file:
        for line in file:
            input_line = line[:-1]

    if len(input_line)%2 == 1:
        input_line = input_line+'0'  #  <-- Hiermit wird an den letzten Datenblock ein leerer, freier Block gesetzt. Hierdurch kann mit mod 2 geloopt werden
    Datenzeile = []
    Indexzeile = []
    for idx in range(int(len(input_line)/2)):  # <-- Loopt über jede Daten-Freiblock Kombination
        Datenzeile.extend([idx]*int(input_line[2*idx]))
        Indexzeile.extend([idx]*int(input_line[2*idx]))
        Datenzeile.extend(['x']*int(input_line[2*idx+1]))

    rev_idx = iter(Indexzeile[::-1])
    Datenzeile = [next(rev_idx) if item == 'x' else item for item in Datenzeile]
    Datenzeile = Datenzeile[:len(Indexzeile)]
    checksum = sum([id * el for id, el in enumerate(Datenzeile)])
    return checksum

def test_problem():
    assert run_problem(test=True) == 1928
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(test=False))
