import math
from queue import PriorityQueue

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
visited = [[False] * N for _ in range(N)]
costs = [[math.inf] * N for _ in range(N)]
costs[0][0] = 0
queue = PriorityQueue()
queue.put((0, (0, 0)))
while queue.qsize() > 0:
  cost, (x1, y1) = queue.get()
  visited[x1][y1] = True
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    x, y = x1 + dx, y1 + dy
    if x >= 0 and y >= 0 and x < N and y < N and not visited[x][y]:
      new_cost = cost + get_grid(x, y)
      if new_cost < costs[x][y]:
        costs[x][y] = new_cost
        queue.put((new_cost, (x, y)))

print(costs[N - 1][N - 1])
