fish = [0] * 9
with open('input-day6.txt') as file:
  line = file.readline().rstrip()
  for k in [int(n) for n in line.split(',')]:
    fish[k] += 1
for d in range(256):
  old_zero = fish[0]
  for i in range(1, 9):
    fish[i - 1] = fish[i]
  fish[8] = old_zero
  fish[6] += old_zero
print(sum(fish))
# print(fish)