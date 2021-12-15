import math

rules = {}
template = None
with open('input-day14.txt') as file:
  template = file.readline().rstrip()
  file.readline()
  while True:
    line = file.readline()
    if len(line) == 0:
      break
    line = line.rstrip()
    parts = line.split(' -> ')
    rules[parts[0]] = parts[1]

freqs = {}
for rule in rules:
  freqs[(rule, 0)] = {}
  freqs[(rule, 0)][rule[0]] = 1
  freqs[(rule, 0)][rule[1]] = freqs[(rule, 0)].get(rule[1], 0) + 1

def add_dict(f1, f2):
  new_f = {}
  for k in f1:
    new_f[k] = new_f.get(k, 0) + f1[k]
  for k in f2:
    new_f[k] = new_f.get(k, 0) + f2[k]
  return new_f

def get_freqs(chunk, step_count):
  if (chunk, step_count) in freqs:
    return freqs[(chunk, step_count)]
  if chunk not in rules:
    freqs[(chunk, step_count)] = {}
    freqs[(chunk, step_count)][chunk[0]] = 1
    freqs[(chunk, step_count)][chunk[1]] = freqs[(chunk, step_count)].get(chunk[1], 0) + 1
    return freqs[(chunk, step_count)]
  c = rules[chunk]
  f1 = get_freqs(chunk[0] + c, step_count - 1)
  f2 = get_freqs(c + chunk[1], step_count - 1)
  f3 = add_dict(f1, f2)
  f3[c] -= 1
  freqs[(chunk, step_count)] = f3
  return freqs[(chunk, step_count)]

STEPS_COUNT = 40
counts = {}
for i in range(len(template) - 1):
  first, second = template[i], template[i + 1]
  counts = add_dict(counts, get_freqs(first + second, STEPS_COUNT))
  if i > 0:
    counts[first] -= 1

maxc, minc = 0, math.inf
for k in counts:
  count = counts[k]
  maxc, minc = max(maxc, count), min(minc, count)
# print(counts)
print(maxc - minc)