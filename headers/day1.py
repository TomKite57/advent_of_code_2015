# -*- coding: utf-8 -*-

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def find_basement(route):
    counter = 0
    floor = 0
    for char in route:
        counter += 1
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return counter


def part1(filename):
    data = readfile(filename)
    answer = data.count('(') - data.count(')')
    print("Final floor is {}.".format(answer))


def part2(filename):
    data = readfile(filename)
    print("First basement encounter on step {}."
          .format(find_basement(data)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day1.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day1.dat")
    timer.checkpoint_hit()

    timer.end_hit()
