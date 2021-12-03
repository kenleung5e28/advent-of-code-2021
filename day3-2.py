lines = []
with open('input-day3.txt') as file:
  for line in file:
    line = line.rstrip()
    lines.append(line)
length = len(lines[0])
data = [l for l in lines]
for i in range(length):
  if len(data) == 1:
    break
  zero_count = 0
  for l in data:
    if l[i] == '0':
      zero_count += 1
  bit = '1' if zero_count <= len(data) - zero_count else '0'
  data = [l for l in data if l[i] == bit]
oxygen = 0
for c in data[0]:
  oxygen = 2 * oxygen + (0 if c == '0' else 1)
data = [l for l in lines]
for i in range(length):
  if len(data) == 1:
    break
  zero_count = 0
  for l in data:
    if l[i] == '0':
      zero_count += 1
  bit = '1' if zero_count > len(data) - zero_count else '0'
  data = [l for l in data if l[i] == bit]
co2 = 0
for c in data[0]:
  co2 = 2 * co2 + (0 if c == '0' else 1)
print(oxygen * co2)