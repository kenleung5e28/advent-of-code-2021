m, n = 0, 0
points = []
folds = []
with open('input-day13.txt') as file:
  while True:
    line = file.readline().rstrip()
    if len(line) == 0:
      break
    x, y = [int(s) for s in line.split(',')]
    m, n = max(m, x), max(n, y)
    points.append((x, y))
  while True:
    line = file.readline()
    if len(line) == 0:
      break
    line = line.rstrip()
    dir, coor = line[len('fold along '):].split('=')
    folds.append((dir, int(coor)))
grid = [[False] * (n + 1) for _ in range(m + 1)]
for x, y in points:
  grid[x][y] = True
for dir, coor in folds[:1]:
  if dir == 'x':
    for x in range(coor + 1, m + 1):
      for y in range(n + 1):
        if grid[x][y]:
          grid[2 * coor - x][y] = True
    m = coor - 1
  elif dir == 'y':
    for x in range(m + 1):
      for y in range(coor + 1, n + 1):
        if grid[x][y]:
          grid[x][2 * coor - y] = True
    n = coor - 1

counts = 0
for x in range(m + 1):
  for y in range(n + 1):
    if grid[x][y]:
      counts += 1
print(counts)