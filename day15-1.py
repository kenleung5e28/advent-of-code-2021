import math

grid = []
with open('input-day15.txt') as file:
  for line in file:
    line = line.rstrip()
    grid.append([int(s) for s in line])
n = len(grid)

costs = [[math.inf] * n for _ in range(n)]
costs[0][0] = 0
queue = [(0, 0)]
while len(queue) > 0:
  x1, y1 = queue.pop(0)
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    x, y = x1 + dx, y1 + dy
    if x >= 0 and y >= 0 and x < n and y < n:
      cost = costs[x1][y1] + grid[x][y]
      if cost < costs[x][y]:
        costs[x][y] = cost
        queue.append((x, y))

print(costs[n - 1][n - 1])