horizontal, depth, aim = 0, 0, 0
with open('input-day2.txt') as file:
  for line in file:
    dir, magnitude = line.rstrip().split(' ')
    magnitude = int(magnitude)
    if dir == 'forward':
      horizontal += magnitude
      depth += aim * magnitude
    elif dir == 'down':
      aim += magnitude
    else:
      aim -= magnitude
print(horizontal * depth)