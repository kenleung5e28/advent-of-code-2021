import re

with open('input-day17.txt') as file:
  input = file.readline().rstrip()

# input = 'target area: x=20..30, y=-10..-5'
m = re.search(r'target area: x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)', input)
x1, x2, y1, y2 = (int(n) for n in m.groups())

def mid_traj(vx: int, vy: int) -> tuple[list[int], int]:
  res = [(0, 0)]
  x, y = 0, 0
  while vx != 0 or vy > 0:
    x += vx
    y += vy
    res.append((x, y))
    if vx < 0:
      vx += 1
    elif vx > 0:
      vx -= 1
    vy -= 1
  return res, vy

def inside(x: int, y: int) -> bool:
  return x >= x1 and x <= x2 and y >= y1 and y <= y2

def valid(vx: int, vy: int) -> tuple[bool, int]:
  traj, term_vy = mid_traj(vx, vy)
  max_y = max([y for _, y in traj])
  for x, y in traj:
    if inside(x, y):
      return True, max_y
  (x, y), vy = traj[-1], term_vy
  count = 0
  while y >= y1:
    count += 1
    y += vy
    if inside(x, y):
      return True, max_y
    vy -= 1
  return False, max_y

count = 0
for vx in range(1, x2 + 1):
  # why the lower and upper bound for y velocity is +-abs(y1)?
  for vy in range(-abs(y1), abs(y1) + 1):
    is_valid, _ = valid(vx, vy)
    if is_valid:
      count += 1
print(count)

