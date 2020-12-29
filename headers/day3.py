# -*- coding: utf-8 -*-

from aoc_tools.advent_timer import Advent_Timer


direc_dict = {'^': (0, 1),
              '>': (1, 0),
              '<': (-1, 0),
              'v': (0, -1)}


def readfile(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


def add_coord(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def get_house_coords(path, start=(0, 0)):
    coords = set([start, ])
    for rule in path:
        start = add_coord(start, direc_dict[rule])
        coords.add(start)
    return coords


def part1(filename):
    data = readfile(filename)
    houses_visited = get_house_coords(data)
    print("Houses that got at least one present: {}."
          .format(len(houses_visited)))


def part2(filename):
    data = readfile(filename)
    houses_visited = get_house_coords(data[0::2])
    houses_visited = houses_visited.union(get_house_coords(data[1::2]))
    print("Houses that got at least one present: {}."
          .format(len(houses_visited)))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../data/day3.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../data/day3.dat")
    timer.checkpoint_hit()

    timer.end_hit()
