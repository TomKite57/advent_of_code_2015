# -*- coding: utf-8 -*-

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [process_line(line) for line in file]


def process_line(str_in):
    if 'turn off' in str_in:
        code = -1
        str_in = str_in.strip('turn off ')
    elif 'turn on' in str_in:
        code = 1
        str_in = str_in.strip('turn on ')
    elif 'toggle' in str_in:
        code = 0
        str_in = str_in.strip('toggle ')

    range1, range2 = [[int(num) for num in rang.split(',')]
                      for rang in str_in.split(' through ')]
    return [code, range1, range2]


def turn_on_p1(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            grid[y][x] = 1
    return grid


def turn_off_p1(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            grid[y][x] = 0
    return grid


def toggle_p1(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            grid[y][x] = 1 - grid[y][x]
    return grid


action_dict_p1 = {-1: turn_off_p1,
                  0: toggle_p1,
                  1: turn_on_p1}


def turn_on_p2(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            grid[y][x] += 1
    return grid


def turn_off_p2(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            if grid[y][x] > 0:
                grid[y][x] -= 1
    return grid


def toggle_p2(range1, range2, grid):
    for x in range(range1[0], range2[0]+1):
        for y in range(range1[1], range2[1]+1):
            grid[y][x] += 2
    return grid


action_dict_p2 = {-1: turn_off_p2,
                  0: toggle_p2,
                  1: turn_on_p2}


def part1(filename):
    data = readfile(filename)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in data:
        grid = action_dict_p1[line[0]](line[1], line[2], grid)
    print("There are {} lights on after the show."
          .format(sum([sum(line) for line in grid])))


def part2(filename):
    data = readfile(filename)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in data:
        grid = action_dict_p2[line[0]](line[1], line[2], grid)
    print("There are {} lights on after the show."
          .format(sum([sum(line) for line in grid])))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day6.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day6.dat")
    timer.checkpoint_hit()

    timer.end_hit()
