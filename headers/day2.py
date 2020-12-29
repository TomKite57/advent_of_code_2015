# -*- coding: utf-8 -*-

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [[int(x) for x in line.split('x')] for line in file]
    return lines


def paper_required(dimensions):
    l, w, h = dimensions
    return 2*(l*w + l*h + w*h) + min(l*w, l*h, w*h)


def ribbon_required(dimensions):
    l, w, h = dimensions
    total = 0
    for dim in sorted(dimensions)[:-1]:
        total += 2*dim
    return total + l*w*h


def part1(filename):
    data = readfile(filename)
    answer = sum([paper_required(line) for line in data])
    print("Total paper to order: {} square feet.".format(answer))


def part2(filename):
    data = readfile(filename)
    answer = sum([ribbon_required(line) for line in data])
    print("Total ribbon to order: {} feet.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day2.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day2.dat")
    timer.checkpoint_hit()

    timer.end_hit()
