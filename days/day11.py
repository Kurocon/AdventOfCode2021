import copy
from collections import defaultdict
from typing import List, Tuple

from days import AOCDay, day


@day(11)
class Day11(AOCDay):
    print_debug = "c12"
    test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

    grid = defaultdict(int)

    def common(self, input_data):
        self.grid = defaultdict(int)
        for y, line in enumerate(input_data):
            for x, i in enumerate(line):
                self.grid[(x, y)] = int(i)

    def increase_all(self) -> List[Tuple[int, int]]:
        flashpoints = []
        for key in self.grid.keys():
            self.grid[key] += 1
            if self.grid[key] > 9:
                flashpoints.append(key)
        return flashpoints

    def neighbours(self, key) -> List[Tuple[int, int]]:
        return [(key[0] + dx, key[1] + dy) for dx, dy in [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ] if (key[0] + dx, key[1] + dy) in self.grid.keys()]

    def process(self, flashpoints) -> int:
        stack = copy.deepcopy(flashpoints)
        seen = set(copy.deepcopy(flashpoints))
        while stack:
            key = stack.pop()
            for nkey in self.neighbours(key):
                self.grid[nkey] += 1
                if nkey not in seen and self.grid[nkey] > 9:
                    seen.add(nkey)
                    stack.append(nkey)
        for key in seen:
            self.grid[key] = 0
        return len(seen)

    def part1(self, input_data):
        total_flashes = 0
        for i in range(100):
            flashpoints = self.increase_all()
            n_flashes = self.process(flashpoints)
            total_flashes += n_flashes
        yield total_flashes

    def part2(self, input_data):
        i = 0
        while True:
            i += 1
            flashpoints = self.increase_all()
            n_flashes = self.process(flashpoints)
            if n_flashes == 100:
                break
        yield i
