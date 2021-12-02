from days import AOCDay, day


@day(2)
class Day2(AOCDay):
    print_debug = "c12"
    test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

    depth = 0
    aim = 0
    x = 0

    def common(self, input_data):
        self.input_data = []

        for line in input_data:
            cmd, amount = line.split()
            self.input_data.append((cmd, int(amount)))

        self.depth, self.aim, self.x = 0, 0, 0

    def part1(self, input_data):
        for cmd, amount in self.input_data:
            if cmd == "forward":
                self.x += amount
            elif cmd == "down":
                self.depth += amount
            elif cmd == "up":
                self.depth -= amount
            else:
                self.error(f"Unknown command {cmd} {amount}")
        yield self.depth * self.x

    def part2(self, input_data):
        for cmd, amount in self.input_data:
            if cmd == "forward":
                self.x += amount
                self.depth += self.aim * amount
            elif cmd == "down":
                self.aim += amount
            elif cmd == "up":
                self.aim -= amount
            else:
                self.error(f"Unknown command {cmd} {amount}")
        yield self.depth * self.x
