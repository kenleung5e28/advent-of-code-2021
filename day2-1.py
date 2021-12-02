horizontal, depth = 0, 0
with open('input-day2.txt') as file:
  for line in file:
    dir, magnitude = line.rstrip().split(' ')
    magnitude = int(magnitude)
    if dir == 'forward':
      horizontal += magnitude
    elif dir == 'down':
      depth += magnitude
    else:
      depth -= magnitude
print(horizontal * depth)