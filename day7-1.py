counts = {}
with open('input-day7.txt') as file:
  line = file.readline().rstrip()
  items = line.split(',')
  for s in items:
    pos = int(s)
    counts[pos] = counts.get(pos, 0) + 1
n = max(counts) + 1
total = sum([i * counts.get(i, 0) for i in range(n)])
target = 0
min_cost = total
for k in range(1, n):
  cost = sum([(k - i) * counts.get(i, 0) for i in range(k)]) + sum([(i - k) * counts.get(i, 0) for i in range(k, n)])
  if cost < min_cost:
    target, min_cost = k, cost
print(target, min_cost)