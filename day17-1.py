import re

def mid_traj(vx, vy) -> tuple[list[int], int]:
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


# with open('input-day17.txt') as file:
#   input = file.readline.rstrip()

input = 'target area: x=20..30, y=-10..-5'
m = re.search(r'target area: x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)', input)
x1, x2, y1, y2 = (int(n) for n in m.groups())

