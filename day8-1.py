total = 0
with open('input-day8.txt') as file:
  for line in file:
    outputs = line.split('|')[1].strip()
    for output in outputs.split(' '):
      if len(output) in [2, 3, 4, 7]:
        total += 1
print(total)