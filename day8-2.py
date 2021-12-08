# 1: cf
# 
# 7: acf
# 
# 4: bcdf
# 
# 2: acdeg
# 3: acdfg
# 5: abdfg
# 
# 0: abcefg
# 6: abdefg
# 9: abcdfg
# 
# 8: abcdefg
# 
# 7 \ 1 => a
# a -> 7 => cf
# cf -> 4 => bd
# a, cf, bd -> 069 => 9, g
# a, cf, g -> 235 => 3, d
# a, bd, g -> 25 => 5, f => 2
# d -> bd => b
# f -> cf => c
# a, b, c, f, g -> 06 => 0, e => 6

def remove(s1, s2):
  s = s1
  for c in s2:
    s = s.replace(c, '')
  return s

def pick(digit_list, remove_list):
  for digit in digit_list:
    removed = remove(digit, ''.join(remove_list))
    if len(removed) == 1:
      return (digit, removed)
  raise ValueError('Cannot single out')

total = 0
with open('input-day8.txt') as file:
  for line in file:
    parts = [s.strip() for s in line.split('|')]
    digits = {'1': None, '4': None, '7': None, '8': None, '235': [], '069': []}
    for s in parts[0].split(' '):
      l = len(s)
      s = ''.join(sorted(s))
      if l == 2:
        digits['1'] = s
      elif l == 3:
        digits['7'] = s
      elif l == 4:
        digits['4'] = s
      elif l == 7:
        digits['8'] = s
      elif l == 5:
        digits['235'].append(s)
      else:
        digits['069'].append(s)
    outputs = [''.join(sorted(s)) for s in parts[1].split(' ')]
    mapping = {}
    # step 1
    mapping['a'] = remove(digits['7'], digits['1'])
    # step 2
    mapping['cf'] = remove(digits['7'], mapping['a'])
    # step 3
    mapping['bd'] = remove(digits['4'], mapping['cf'])
    # step 4
    digits['9'], mapping['g'] = pick(digits['069'], [mapping['a'], mapping['bd'], mapping['cf']])
    # step 5
    digits['3'], mapping['d'] = pick(digits['235'], [mapping['a'], mapping['cf'], mapping['g']])
    # step 6
    digits['25'] = [d for d in digits['235'] if d != digits['3']]
    digits['5'], mapping['f'] = pick(digits['235'], [mapping['a'], mapping['bd'], mapping['g']])
    digits['2'] = [d for d in digits['25'] if d != digits['5']][0]
    # step 7
    mapping['b'] = remove(mapping['bd'], mapping['d'])
    # step 8
    mapping['c'] = remove(mapping['cf'], mapping['f'])
    # step 9
    digits['06'] = [d for d in digits['069'] if d != digits['9']]
    digits['0'], mapping['e'] = pick(digits['06'], [mapping['a'], mapping['b'], mapping['c'], mapping['f'], mapping['g']])
    digits['6'] = [d for d in digits['06'] if d != digits['0']][0]
    answer = []
    for output in outputs:
      for i in digits:
        if output == digits[i]:
          answer.append(i)
          break
    total += int(''.join(answer))
print(total)