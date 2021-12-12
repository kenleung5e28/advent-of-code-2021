from collections import defaultdict

adj = defaultdict(list)
with open('input-day12.txt') as file:
  for line in file:
    line = line.rstrip()
    parts = line.split('-')
    adj[parts[0]].append(parts[1])
    adj[parts[1]].append(parts[0])

paths = []

def trace(path: list[str], curr: str) -> None:
  if curr == 'end':
    paths.append(path)
    return
  for nb in adj[curr]:
    if nb != curr and (nb.isupper() or nb not in path):
      trace([*path, curr], nb)

trace([], 'start')
print(len(paths))
