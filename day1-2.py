nums = []
with open('input-day1.txt') as file:
  for line in file:
    nums.append(int(line.rstrip()))
start, end, count = 0, 3, 0
while end < len(nums):
  if nums[end] > nums[start]:
    count += 1
  start += 1
  end += 1
print(count)
