# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 10.12.2024 - nachgereicht am 11.12.


def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    topography = []

    with open(input_doc, 'r') as file:
        for line in file:
            topography.append(line[:-1])

    overall_score = 0
    for line_ind, line in enumerate(topography):
        zero_indices = [i for i, x in enumerate(line) if x == '0']
        for zi in zero_indices:
            niners = search_node(line_ind, zi, topography)
            overall_score += len(set(niners))
    return overall_score

def search_node(l, c, topography):
    score = [] 
    magnitude = int(topography[l][c])
    if magnitude == 9:
        score.append(tuple((l, c)))
        return score 
    if l > 0 and magnitude-int(topography[l-1][c]) == -1:
        score.extend(search_node(l-1, c, topography))
    if c > 0 and magnitude-int(topography[l][c-1]) == -1:
        score.extend(search_node(l, c-1, topography))
    if l < len(topography) - 1 and magnitude-int(topography[l+1][c]) == -1:
        score.extend(search_node(l+1, c, topography))
    if c < len(topography[0]) - 1 and magnitude-int(topography[l][c+1]) == -1:
        score.extend(search_node(l, c+1, topography))
    return score


def test_problem():
    assert run_problem(test=True) == 36
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(test=False))
