import math

def parse_literal(s: str, start: int) -> tuple[int, int]:
  p, num = start, ''
  while True:
    done = s[p] == '0'
    num += s[(p + 1):(p + 5)]
    p += 5
    if done:
      break
  return int(num, base=2), p

def next_ptr(p: int) -> int:
  mod = p % 4
  offset = 0 if mod == 0 else 4 - mod
  return p + offset


def parse_packet(s: str, start: int) -> tuple[dict, int]:
  p = start
  version = int(s[p:(p + 3)], base=2)
  p += 3
  id = int(s[p:(p + 3)], base=2)
  p += 3
  isLiteral = id == 4
  packet = {
    'version': version,
    'id': id,
    'isLiteral': isLiteral,
  }
  if isLiteral:
    value, p = parse_literal(s, p)
    return packet | {
      'value': value,
    }, p
  else:
    subpackets = []
    if s[p] == '0':
      p += 1
      length = int(s[p:(p + 15)], base=2)
      p += 15
      end = p + length
      while p < end:
        subpacket, p = parse_packet(s, p)
        subpackets.append(subpacket)
    else:
      p += 1
      count = int(s[p:(p + 11)], base=2)
      p += 11
      for _ in range(count):
        subpacket, p = parse_packet(s, p)
        subpackets.append(subpacket)
    return packet | {
      'subpackets': subpackets
    }, p

digits = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111',
}
input = None
with open('input-day16.txt') as file:
  input = file.readline().rstrip()

def parse(s: str) -> dict:
  return parse_packet(''.join([digits[c] for c in s]), 0)[0]

def eval(packet: dict) -> int:
  if packet['isLiteral']:
    return packet['value']
  id, subpackets = packet['id'], packet['subpackets']
  values = [eval(subpacket) for subpacket in subpackets]
  if id == 0:
    return sum(values)
  if id == 1:
    return math.prod(values)
  if id == 2:
    return min(values)
  if id == 3:
    return max(values)
  if id == 5:
    return 1 if values[0] > values[1] else 0
  if id == 6:
    return 1 if values[0] < values[1] else 0
  return 1 if values[0] == values[1] else 0

print(eval(parse(input)))
