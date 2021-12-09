def is_low_point(map: list[list[int]], x: int, y: int) -> bool:
  m, n = len(map), len(map[0])
  val = map[x][y]
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    x1, y1 = x + dx, y + dy
    if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and val >= map[x1][y1]:
      return False
  return True

map = []
with open('input-day9.txt') as file:
  for line in file:
    line = line.rstrip()
    map.append([int(c) for c in line])
total_risk = 0
for x in range(len(map)):
  for y in range(len(map[0])):
    if is_low_point(map, x, y):
      total_risk += map[x][y] + 1
print(total_risk)