with open('day1/input.txt', 'r') as f:
  sum = 0
  for line in f.readlines():
    digits = list(filter(lambda x: x.isdigit(), list(line.strip())))
    sum += 10 * int(digits[0]) + int(digits[-1])
  print(sum)