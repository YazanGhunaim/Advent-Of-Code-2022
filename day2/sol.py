# get input from file

with open('inp.txt') as file:
    list_of_moves = [i for i in file.read().split('\n')]

# hashmap/dictionary
my_dict_part1 = {"A X": 4, "A Y": 8, "A Z": 3,
                 "B X": 1, "B Y": 5, "B Z": 9,
                 "C X": 7, "C Y": 2, "C Z": 6}


my_dict_part2 = {"A X": 3, "A Y": 4, "A Z": 8,
                 "B X": 1, "B Y": 5, "B Z": 9,
                 "C X": 2, "C Y": 6, "C Z": 7}
# list comprehension
list_of_moves_part1 = [my_dict_part1.get(x, x) for x in list_of_moves]
list_of_moves_part2 = [my_dict_part2.get(x, x) for x in list_of_moves]

# removing empty strings in list of moves

while ("" in list_of_moves_part1):
    list_of_moves_part1.remove("")

while ("" in list_of_moves_part2):
    list_of_moves_part2.remove("")
	

sumPT1 = sum(list_of_moves_part1)
sumPT2 = sum(list_of_moves_part2)

print(sumPT1)
print(sumPT2)

"""
------- Part 1 -------
psuedocode:

	1 pt -> rock 'X'
	2 pt -> paper 'Y'
	3 pt -> scissors 'Z'

	0 pt -> L
	3 pt -> D
	6 pt -> W
	
9 possibilities:

1:	"A X", 4
2:	"A Y", 8
3:	"A Z", 3
4:	"B X", 1
5:	"B Y", 5
6:	"B Z", 9
7:	"C X", 7
8:	"C Y", 2
9:	"C Z", 6

------- Part 2 -------


"""
