def get_points(x1, y1, x2, y2, dx, dy):
  points = []
  x, y = x1, y1
  while x != x2 or y != y2:
    points.append((x, y))
    x += dx
    y += dy
  points.append((x2, y2))
  return points

freq = {}
total = 0
with open('input-day5.txt') as file:
  for line in file:
    line = line.rstrip()
    p1, p2 = line.split(' -> ')
    x1, y1 = tuple(int(n) for n in p1.split(','))
    x2, y2 = tuple(int(n) for n in p2.split(','))
    dx, dy = None, None
    if x1 == x2:
      dx = 0
      dy = 1 if y1 < y2 else -1
    elif y1 == y2:
      dx = 1 if x1 < x2 else -1
      dy = 0
    else:
      dx = 1 if x1 < x2 else -1
      dy = 1 if y1 < y2 else -1
    points = get_points(x1, y1, x2, y2, dx, dy)
    #print(points)
    for x, y in points:
      value = freq.get((x, y), 0)
      freq[(x, y)] = value + 1
      if freq[(x, y)] == 2:
        total += 1
#print(freq)
print(total)