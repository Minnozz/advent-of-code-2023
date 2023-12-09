import re

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

part1 = 0
line_format = re.compile(r"^Game (\d+): (.+)$")

with open("day2/input.txt", "r") as f:
    for line in f.readlines():
        m = line_format.search(line)
        game_number = int(m.group(1))
        possible = True
        for draw in m.group(2).split("; "):
            for cubes in draw.split(", "):
                [n, color] = cubes.split(" ")
                if int(n) > maximums[color]:
                    possible = False
                    break
        if possible:
            part1 += game_number

print("part 1 sum: {}".format(part1))
