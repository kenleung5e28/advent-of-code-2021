prev, curr = None, None
count = 0
with open('input-day1.txt') as file:
  for line in file:
    prev, curr = curr, int(line.rstrip())
    if prev is not None and curr > prev:
      count += 1
print(count)
