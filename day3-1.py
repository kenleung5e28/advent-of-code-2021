line_count = 0
length = None
zero_counts = None
with open('input-day3.txt') as file:
  for line in file:
    line = line.rstrip()
    if length is None:
      length = len(line)
      zero_counts = [0] * length
    line_count += 1
    for i in range(length):
      if line[i] == '0':
        zero_counts[i] += 1
gamma = 0
epsilon = 0
for z in zero_counts:
  gamma = 2 * gamma + (0 if z > line_count - z else 1)
  epsilon = 2 * epsilon + (1 if z > line_count - z else 0)
print(gamma * epsilon)