import math

def manhattanDistance(puzzle, solution, size):
	ret = 0
	for i in range(size * size):
		if puzzle[i] != 0 and puzzle[i] != solution[i]:
			sol_i = solution.index(puzzle[i])
			y = (i // size) - (sol_i // size)
			x = (i % size) - (sol_i % size)
			ret += abs(y) + abs(x)
	return ret

def hammingDistance(puzzle, solution, size):
	ret = 0
	for i in range(size * size):
		if puzzle[i] != 0 and puzzle[i] != solution[i]:
			ret += 1
	return ret

def euclideanDistance(puzzle, solution, size):
	ret = 0
	for i in range(size * size):
		if puzzle[i] != 0 and puzzle[i] != solution[i]:
			sol_i = solution.index(puzzle[i])
			y = (i // size) - (sol_i // size)
			x = (i % size) - (sol_i % size)
			ret += math.sqrt(y**2 + x**2)
	return ret

def uniform(puzzle, solution, size):
	return 0

HEURISTICS = {
	"manhattan" : manhattanDistance,
	"hamming" : hammingDistance,
	"euclidean": euclideanDistance
}
