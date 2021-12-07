from days import AOCDay, day


@day(7)
class Day7(AOCDay):
    print_debug = "c12"
    test_input = """16,1,2,0,4,2,7,1,2,14"""

    horizontal_positions = []

    def common(self, input_data):
        self.horizontal_positions = list(map(int, input_data.split(',')))

    def part1(self, input_data):
        smallest_fuel = None
        for align_pos in range(min(self.horizontal_positions), max(self.horizontal_positions) + 1):
            total_fuel = sum(abs(align_pos - pos) for pos in self.horizontal_positions)
            if smallest_fuel is None or total_fuel < smallest_fuel:
                smallest_fuel = total_fuel
        yield smallest_fuel

    def part2(self, input_data):
        smallest_fuel = None
        for align_pos in range(min(self.horizontal_positions), max(self.horizontal_positions) + 1):
            total_fuel = sum(sum(range(abs(align_pos - pos) + 1)) for pos in self.horizontal_positions)
            if smallest_fuel is None or total_fuel < smallest_fuel:
                smallest_fuel = total_fuel
        yield smallest_fuel
