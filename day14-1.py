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
for i in range(10):
  next = template[0]
  for j in range(len(template) - 1):
    chunk = template[j:(j + 2)]
    if chunk in rules:
      next += rules[chunk] + chunk[1]
    else:
      next += chunk[1]
  template = ''.join(next)
freqs = {}
for c in template:
  freqs[c] = freqs.get(c, 0) + 1
maxfreq, minfreq = 0, math.inf
for k in freqs:
  freq = freqs[k]
  maxfreq, minfreq = max(maxfreq, freq), min(minfreq, freq)
print(maxfreq - minfreq)