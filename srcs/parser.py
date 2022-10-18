import argparse
from srcs.heuristics import HEURISTICS
from srcs.solution_generator import SOLUTIONS

def parse_file(argv):
	file = argv
	with open(file, 'r') as f:
		lines = f.readlines()
	count_i = 0
	count_j = 0
	size =  0
	puzzle = []
	for line in lines:
		if line[0] == '#':
			pass
		elif len(line.split()) == 1:
			size = int(line)
		else:
			row = []
			for i in line.split():
				if i.isdigit():
					row.append(int(i))
					count_j += 1
			puzzle.append(row)
			count_i += 1
	puzzle1D = []
	for row in puzzle:
		for elem in row:
			puzzle1D.append(elem)
	generated = [x for x in range(size ** 2)]
	difference = [x for x in generated if x not in puzzle1D]
	
	if len(difference) != 0:
		exit("Error: The file is not correctly formatted")
	if count_i != size or size == 0 or count_j != size * size or size < 3:
		exit("Error: The file is not correctly formatted")
	return tuple(puzzle1D), size

def parse():
	parser = argparse.ArgumentParser(description="n-puzzle @ jvaquer 42")
	parser.add_argument("file", help="input puzzle file")
	parser.add_argument("-g", "--greedy", action="store_true", help="greedy search")
	parser.add_argument("-u", "--uniform", action="store_true", help="uniform-cost search")
	parser.add_argument("-a", "--algorithm", choices=HEURISTICS.keys(), default="manhattan")
	parser.add_argument("-s", "--solution", choices=SOLUTIONS.keys(), default="snail")
	args = parser.parse_args()
	return args
