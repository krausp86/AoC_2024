# Advent of Code 2024 - Part 2
# Patrick Kraus-Füreder
# 02.12.2024

def run_problem(test=False):
    if test:
        input_doc = 'test_input_01.txt'
    else:
        input_doc = 'quiz_input_01.txt'

    valid_signals = 0
    with open(input_doc, 'r') as file:
        for line in file:
            signal = [int(n) for n in line.split()]
            diff_signal = [signal[i+1] - signow for i, signow in enumerate(signal[:-1])]
            if is_safe(signal):
                valid_signals += 1
            elif signal_dampener(signal):
                valid_signals += 1
    return valid_signals

def is_safe(signal):
    diff_signal = [signal[i+1] - signow for i, signow in enumerate(signal[:-1])]
    if (all(num < 0 for num in diff_signal) or all(num > 0 for num in diff_signal)) and all(abs(num) < 4 for num in diff_signal):
        return True
    return False

def signal_dampener(signal):
    for i, _ in enumerate(signal):
        working_signal = signal.copy()
        working_signal.pop(i)
        if is_safe(working_signal):
            return True
    return False

def test_run_problem():
    assert run_problem(test=True) == 4

if __name__ == '__main__':
    print(run_problem(test=False))
