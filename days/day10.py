from typing import Tuple, Optional

from days import AOCDay, day


@day(10)
class Day10(AOCDay):
    print_debug = "c12"
    test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

    def common(self, input_data):
        pass

    CLOSING_MAP = {'(': ')', '[': ']', '{': '}', '<': '>'}
    SCORES_MAP = {')': 3, ']': 57, '}': 1197, '>': 25137}
    SCORES_MAP_2 = {')': 1, ']': 2, '}': 3, '>': 4}

    def parse(self, unparsed, parsed) -> Tuple[str, str, str, Optional[str], Optional[str]]:
        while len(unparsed):
            c = unparsed[0]
            if c in "([{<":
                parsed, unparsed = parsed + c, unparsed[1:]
                res, unparsed, parsed, expected, found = self.parse(unparsed, parsed)
                if res != "ok":
                    return res, unparsed, parsed, expected + self.CLOSING_MAP[c], found
                if unparsed:
                    if unparsed[0] != self.CLOSING_MAP[c]:
                        return "corrupt", unparsed, parsed, self.CLOSING_MAP[c], unparsed[0]
                    parsed, unparsed = parsed + unparsed[0], unparsed[1:]
                else:
                    # Nothing to parse but still expecting!
                    return "incomplete", unparsed, parsed, self.CLOSING_MAP[c], None
            elif c in ")]}>":
                return "ok", unparsed, parsed, None, c
        return "ok", unparsed, parsed, None, None

    def part1(self, input_data):
        res = 0
        for line in self.input_data:
            result, unparsed, parsed, expected, found = self.parse(line, "")
            if result == "corrupt":
                res += self.SCORES_MAP[found]
        yield res

    def part2(self, input_data):
        scores = []
        for line in self.input_data:
            result, unparsed, parsed, expected, found = self.parse(line, "")
            if result == "incomplete":
                score = 0
                for char in expected:
                    score = score * 5 + self.SCORES_MAP_2[char]
                scores.append(score)
        yield sorted(scores)[len(scores)//2]
