# -*- coding: utf-8 -*-

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def vowel_condition(str_in, lower_lim=3):
    total = 0
    for vowel in 'aeiou':
        total += str_in.count(vowel)
    return total >= lower_lim


def double_letter_condition(str_in):
    prev_char = str_in[0]
    for char in str_in[1:]:
        if char == prev_char:
            return True
        prev_char = char
    return False


def avoid_pair_condition(str_in):
    for pair in ['ab', 'cd', 'pq', 'xy']:
        if str_in.count(pair):
            return False
    return True


def nice_str_p1(str_in):
    return vowel_condition(str_in) and\
            double_letter_condition(str_in) and\
            avoid_pair_condition(str_in)


def repeating_pair_condition(str_in):
    prev_char = str_in[0]
    for i, char in enumerate(str_in[1:-2]):
        if prev_char + char in str_in[i+2:]:
            return True
        prev_char = char
    return False


def repeating_letter_condition(str_in):
    for i, char in enumerate(str_in[:-2]):
        if str_in[i+2] == char:
            return True
    return False


def nice_str_p2(str_in):
    return repeating_pair_condition(str_in) and\
            repeating_letter_condition(str_in)


def part1(filename):
    data = readfile(filename)
    num_nice_strings = sum([1 for line in data if nice_str_p1(line)])
    print("There are {} nice strings in total.".format(num_nice_strings))


def part2(filename):
    data = readfile(filename)
    num_nice_strings = sum([1 for line in data if nice_str_p2(line)])
    print("There are {} nice strings in total.".format(num_nice_strings))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day5.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day5.dat")
    timer.checkpoint_hit()

    timer.end_hit()
