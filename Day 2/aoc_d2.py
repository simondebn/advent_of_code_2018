# ADVENT OF CODE 2018
# Day 2 : Inventory Management System #

input_file_path = './aoc_d2_inputs.txt'


# Part 1 #
def aoc_letter_freq_checksum(filepath):
    two_freq_box = 0
    three_freq_box = 0
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            freq = dict()
            for cnt_2, letter in enumerate(line):
                if letter in freq:
                    freq[letter] = freq[letter] + 1
                else:
                    freq[letter] = 1
            two_freq = False
            three_freq = False
            for letter, number in freq.items():
                if two_freq is False and int(number) == 2:
                    two_freq = True
                    two_freq_box = two_freq_box + 1
                elif three_freq is False and int(number) == 3:
                    three_freq = True
                    three_freq_box = three_freq_box + 1
    return two_freq_box * three_freq_box


# Part 2 #
def aoc_find_prototype(filepath):
    protos = {0}
    res = ''
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            with open(filepath) as fp_2:
                for cnt_2, line_2 in enumerate(fp_2):
                    diff = 0
                    proto = ''
                    if line != line_2:
                        i = 0
                        while diff < 2 and line[i] != '\n':
                            letter_1 = line[i]
                            letter_2 = line_2[i]
                            if letter_1 != letter_2:
                                diff = diff + 1
                            else:
                                proto = proto + letter_1
                            i = i + 1
                    if diff == 1 and proto not in protos:
                        protos.add(proto)

    for key, value in enumerate(protos):
        if value != 0:
            res = res + value
    return res


print(aoc_letter_freq_checksum(input_file_path))
print(aoc_find_prototype(input_file_path))
