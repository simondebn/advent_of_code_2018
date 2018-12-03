# ADVENT OF CODE 2018 - DAY 1 #
input_file_path = './aoc_d1_inputs.txt'


# Part 1 #
def aoc_freq(filepath):
    freq = 0
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            freq += int(line)  # if line[0] == '+' else freq - int(line[1:])
    return freq


# Part 2 #
def aoc_freq_redundant(filepath):
    seen = {0}
    freq = 0
    while True:
        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                freq += int(line)
                if freq in seen:
                    return freq
                seen.add(freq)


print(aoc_freq(input_file_path))
print(aoc_freq_redundant(input_file_path))
