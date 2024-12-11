# Advent of Code 2024 - Part 2
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

    index = 0
    Datenzeile = []
    for idx, num in enumerate(input_line):  # <-- Loopt über jede Daten-Freiblock Kombination
        if idx%2 == 1 and int(num) != 0:
            Datenzeile.append(('x', int(num)))
        elif idx%2 == 0:
            Datenzeile.append((index, int(num)))
            index += 1
    for idx in range(index-1, -1, -1):
        d_idx = [i for i, el in enumerate(Datenzeile) if el[0] == idx][0]
        ad_idx = find_fitting_block(Datenzeile[d_idx], Datenzeile)
        if ad_idx is not None and ad_idx < d_idx:
            Datenzeile[ad_idx:ad_idx+1] = put_data_in_block(Datenzeile[ad_idx], Datenzeile[d_idx])
            Datenzeile[d_idx+1] = ('x', Datenzeile[ad_idx][1])

    Datenzeile_neu = []
    for data in Datenzeile:
        if data[0] == 'x':
            Datenzeile_neu.extend(['x']*data[1])
        else:
            Datenzeile_neu.extend([data[0]]*data[1])
    checksum = 0
    for idx, num in enumerate(Datenzeile_neu):
        if num != 'x':
            checksum += idx*num
    return checksum

def fits_in_block(block, data):
    if block[1] >= data[1]:
        return True
    return False

def put_data_in_block(block, data):
    return data, (block[0], block[1]-data[1])

def find_fitting_block(data, all_data):
    for bl_id, block in enumerate(all_data):
        if block[0]=='x' and fits_in_block(block, data):
            return bl_id
    return None

def test_problem():
    assert run_problem(test=True) == 2858
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(test=False))
