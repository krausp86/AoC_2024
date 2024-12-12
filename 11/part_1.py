# Advent of Code 2024 - Part 1
# Patrick Kraus-Füreder
# 11.12.2024


def run_problem(iterations=1, test=False):
    if test:
        stone_list = ['125', '17']
    else:
        stone_list = ['475449', '2599064', '213', '0', '2', '65', '5755', '51149']

    for it in range(iterations):
        new_stone_list = []
        for stone in stone_list:
            if int(stone) == 0:
                new_stone_list.append('1')
            elif len(stone) % 2 == 0:
                new_stone_list.append(str(int(stone[:int(len(stone)/2)])))
                new_stone_list.append(str(int(stone[int(len(stone)/2):])))
            else:
                new_stone_list.append(str(int(stone)*2024))
        stone_list = new_stone_list
    return len(stone_list)

def test_problem():
    assert run_problem(6, test=True) == 22
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(25, test=False))
