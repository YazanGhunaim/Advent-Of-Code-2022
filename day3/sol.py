# Getting the data
from string import ascii_letters

with open("inp.in") as file:
	data = [i for i in file.read().strip().split("\n")]

totalSum = 0
# iterate through data
for rucksack in data:
	# find half
	half = len(rucksack)//2

	left = set(rucksack[:half])
	right = set(rucksack[half:])

	# print(rucksack, left, right)
	for priority, char in enumerate(ascii_letters):
		if char in left and char in right:
			totalSum += priority + 1

print("Answer to part 1: ", totalSum)

# part 2

j = 3
totalSumTwo = 0
for i in range(0, len(data), 3):
	rucksacks = data[i:j]
	j += 3

	for priority, char in enumerate(ascii_letters):
		if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
			totalSumTwo += priority + 1

print("Answer to pt 2: ", totalSumTwo)




