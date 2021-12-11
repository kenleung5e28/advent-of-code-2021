
opening = {')': '(', ']': '[', '}': '{', '>': '<'}
corrupted_counts = {')': 0, ']' : 0, '}': 0, '>': 0}
with open('input-day10.txt') as file:
  for line in file:
    stack = []
    for c in line:
      if c in ['(', '[', '{', '<']:
        stack.append(c)
      elif c in [')', ']', '}', '>']:
        if len(stack) == 0 or stack.pop() != opening[c]:
          corrupted_counts[c] += 1
          break
marks = {')': 3, ']' : 57, '}': 1197, '>': 25137}
print(sum([corrupted_counts[c] * marks[c] for c in [')', ']', '}', '>']]))