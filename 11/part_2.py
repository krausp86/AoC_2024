# Advent of Code 2024 - Part 2
# Patrick Kraus-Füreder
# 11.12.2024


def run_problem(iterations=1, test=False):
    if test:
        stone_list = ['125', '17']
    else:
        stone_list = ['475449', '2599064', '213', '0', '2', '65', '5755', '51149']

    stone_dict = {}
    for stone in stone_list:
        stone_dict[stone] = 1

    for iter in range(iterations):
        new_stone_dict = {}
        for stone in stone_dict.keys():
            if stone == '0':
                new_stone_dict['1'] = new_stone_dict.get('1', 0) + stone_dict[stone]
            elif len(stone)%2 == 0:
                half_point_key = int(len(stone)/2) 
                upper_value_default = new_stone_dict.get(stone[:half_point_key], 0)
                new_stone_dict[stone[:half_point_key]] = upper_value_default + stone_dict[stone]

                new_remainder = stone[half_point_key:].lstrip('0')
                new_remainder = new_remainder if new_remainder != '' else '0'
                lower_value_default = new_stone_dict.get(new_remainder, 0)
                new_stone_dict[new_remainder] = lower_value_default + stone_dict[stone]
            else:
                new_stone_dict[str(int(stone)*2024)] = new_stone_dict.get(str(int(stone)*2024), 0) + stone_dict[stone]
        stone_dict = new_stone_dict
    return sum(stone_dict.values())

def test_problem():
    assert run_problem(6, test=True) == 22
    print('Test passed')

if __name__ == '__main__':
    print(run_problem(75, test=False))
