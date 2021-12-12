from collections import defaultdict

from days import AOCDay, day


@day(12)
class Day12(AOCDay):
    print_debug = "c12"
    test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")
    test_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split("\n")
    test_input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split("\n")

    caves = defaultdict(list)

    def common(self, input_data):
        data = [line.split("-") for line in input_data]
        self.caves = defaultdict(list)
        for start, end in data:
            if start != "start":
                self.caves[end].append(start)
            if end != "start":
                self.caves[start].append(end)

    def dfs(self, last, seen, edges, allow_repeats):
        if last == "end":
            return 1
        paths = 0
        for edge in edges[last]:
            # Any node that is not lowercase and already seen, go on processing
            if not (edge.islower() and edge in seen):
                paths += self.dfs(edge, seen | {edge}, edges, allow_repeats)
            # Any node that IS lowercase and already seen can only go one time on if repeats are allowed.
            elif edge.islower() and edge in seen and allow_repeats:
                paths += self.dfs(edge, seen | {edge}, edges, False)
        return paths

    def part1(self, input_data):
        yield self.dfs("start", set(), self.caves, False)

    def part2(self, input_data):
        yield self.dfs("start", set(), self.caves, True)
