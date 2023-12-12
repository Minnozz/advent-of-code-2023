import re

numbers = re.compile(r"(\d+)")

with open("day3/input.txt", "r") as f:
    lines = list(map(lambda line: line.strip(), f))

    def is_symbol(line_idx, idx):
        try:
            char = lines[line_idx][idx]
            return not (char.isdigit() or char == ".")
        except IndexError:
            return False

    def touches_symbol(line_idx, span):
        span_from, span_to = span
        for y in range(line_idx - 1, line_idx + 2):
            for x in range(span_from - 1, span_to + 1):
                if is_symbol(y, x):
                    return True
        return False

    part1 = 0

    for line_idx, line in enumerate(lines):
        for m in numbers.finditer(line):
            if touches_symbol(line_idx, m.span()):
                part1 += int(m.group(1))

    print("part 1 sum: {}".format(part1))
