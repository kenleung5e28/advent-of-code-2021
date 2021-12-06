fish = []
with open('input-day6.txt') as file:
  line = file.readline().rstrip()
  fish = [int(n) for n in line.split(',')]
for d in range(80):
  for i in range(len(fish)):
    if fish[i] > 0:
      fish[i] -= 1
    else:
      fish[i] = 6
      fish.append(8)
print(len(fish))