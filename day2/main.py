import re

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

line_format = re.compile(r"^Game (\d+): (.+)$")

part1 = 0
part2 = 0

with open("day2/input.txt", "r") as f:
    for line in f.readlines():
        m = line_format.search(line)
        game_number = int(m.group(1))
        possible = True
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for draw in m.group(2).split("; "):
            for cubes in draw.split(", "):
                [n_str, color] = cubes.split(" ")
                n = int(n_str)

                # part 1
                if n > maximums[color]:
                    possible = False

                # part 2
                minimums[color] = max(minimums[color], n)

        # part 1
        if possible:
            part1 += game_number

        # part 2
        power = minimums["red"] * minimums["green"] * minimums["blue"]
        part2 += power

print("part 1 sum: {}".format(part1))
print("part 2 sum: {}".format(part2))
