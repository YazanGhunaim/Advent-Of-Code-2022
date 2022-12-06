# open the input file
with open ('inp.txt') as file:
        data = [i for i in file.read().strip().split('\n')]

calories = []
count = 0
max = 0
for item in data:
    i = 0
    if item == '':
        calories.insert(i,count)
        i += 1
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count

calories.sort(reverse= True)
sum = 0
for i in range(3):
    sum += calories[i]


print(sum)