from collections import defaultdict

adj = defaultdict(list)
with open('input-day12.txt') as file:
  for line in file:
    line = line.rstrip()
    parts = line.split('-')
    adj[parts[0]].append(parts[1])
    adj[parts[1]].append(parts[0])

paths = []

def trace(path: list[str], curr: str, visited_twice: bool) -> None:
  if curr == 'end':
    paths.append(path)
    return
  for nb in adj[curr]:
    if nb != curr:
      if nb.isupper():
        trace([*path, curr], nb, visited_twice)
      elif visited_twice:
        if nb not in path:
          trace([*path, curr], nb, True)
      else:
        if nb not in path:
          trace([*path, curr], nb, False)
        elif nb not in ['start', 'end']:
          trace([*path, curr], nb, True)

trace([], 'start', False)
print(len(paths))
