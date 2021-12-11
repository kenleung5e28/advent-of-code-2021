grid = []
with open('input-day11.txt') as file:
  for line in file:
    line = line.rstrip()
    grid.append([int(c) for c in line])
m, n = len(grid), len(grid[0])

def advance():
  queue = []
  for x in range(m):
    for y in range(n):
      grid[x][y] += 1
      if grid[x][y] == 10:
        grid[x][y] = 0
        queue.append((x, y))
  while len(queue) > 0:
    x0, y0 = queue.pop(0)
    for dx, dy in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
      x, y = x0 + dx, y0 + dy
      if x < 0 or y < 0 or x >= m or y >= n:
        continue
      if grid[x][y] > 0:
        grid[x][y] += 1
        if grid[x][y] == 10:
          grid[x][y] = 0
          queue.append((x, y))

count = 0
for _ in range(100):
  advance()
  for x in range(m):
    for y in range(n):
      if grid[x][y] == 0:
        count += 1
print(count)
