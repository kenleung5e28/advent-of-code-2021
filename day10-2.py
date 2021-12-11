
opening = {')': '(', ']': '[', '}': '{', '>': '<'}
marks = {'(': 1, '[' : 2, '{': 3, '<': 4}
scores = []
with open('input-day10.txt') as file:
  for line in file:
    stack = []
    corrupted = False
    for c in line:
      if c in ['(', '[', '{', '<']:
        stack.append(c)
      elif c in [')', ']', '}', '>']:
        if len(stack) == 0 or stack.pop() != opening[c]:
          corrupted = True
          break
    if corrupted:
      continue
    score = 0
    while len(stack) > 0:
      score = 5 * score + marks[stack.pop()]
    if score > 0:
      scores.append(score)
scores.sort()
print(scores[len(scores) // 2])