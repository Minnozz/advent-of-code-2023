words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

with open("day1/input.txt", "r") as f:
    part1 = 0
    part2 = 0
    for line in f.readlines():
        line = line.strip()

        # Part 1
        digits = list(filter(lambda x: x.isdigit(), list(line)))
        part1 += 10 * int(digits[0]) + int(digits[-1])

        # Part 2
        firsts = []
        lasts = []
        for n, word in enumerate(words):
            firsts.append([line.find(word), n])
            firsts.append([line.find(str(n)), n])
            lasts.append([line.rfind(word), n])
            lasts.append([line.rfind(str(n)), n])
        first = min(filter(lambda tup: tup[0] != -1, firsts))[1]
        last = max(filter(lambda tup: tup[0] != -1, lasts))[1]
        part2 += 10 * int(first) + int(last)

    print("part 1 sum: {}".format(part1))
    print("part 2 sum: {}".format(part2))
