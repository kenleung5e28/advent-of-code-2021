import math

grid = []
with open('input-day15.txt') as file:
  for line in file:
    line = line.rstrip()
    grid.append([int(s) for s in line])
n = len(grid)

def get_grid(x, y):
  qx, qy = x // n, y // n
  rx, ry = x % n, y % n
  val = grid[rx][ry] + qx + qy
  return val % 10 + 1 if val > 9 else val

N = 5 * n
costs = [[math.inf] * N for _ in range(N)]
costs[0][0] = 0
queue = [(0, 0)]
while len(queue) > 0:
  x1, y1 = queue.pop(0)
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    x, y = x1 + dx, y1 + dy
    if x >= 0 and y >= 0 and x < N and y < N:
      cost = costs[x1][y1] + get_grid(x, y)
      if cost < costs[x][y]:
        costs[x][y] = cost
        queue.append((x, y))

print(costs[N - 1][N - 1])
