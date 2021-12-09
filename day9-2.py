def is_low_point(map: list[list[int]], x: int, y: int) -> bool:
  m, n = len(map), len(map[0])
  val = map[x][y]
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    x1, y1 = x + dx, y + dy
    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and val >= map[x1][y1]:
      return False
  return True

def fill(map: list[list[int]], basin: set, x: int, y: int) -> None:
  m, n = len(map), len(map[0])
  val = map[x][y]
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    x1, y1 = x + dx, y + dy
    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and map[x1][y1] < 9 and map[x1][y1] - val >= 1:
      basin.add((x1, y1))
      fill(map, basin, x1, y1)

map = []
with open('input-day9.txt') as file:
  for line in file:
    line = line.rstrip()
    map.append([int(c) for c in line])
low_points = []
for x in range(len(map)):
  for y in range(len(map[0])):
    if is_low_point(map, x, y):
      low_points.append((x, y))
basins = []
for x0, y0 in low_points:
  basin = set([(x0, y0)])
  fill(map, basin, x0, y0)
  basins.append(basin)
basins.sort(key=len, reverse=True)
sizes = [len(basin) for basin in basins]
print(sizes[0] * sizes[1] * sizes[2])