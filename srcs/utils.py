def print_puzzle(puzzle, size):
	count = 0
	for i in puzzle:
		print(i, end="")
		if i / 10 < 1.0 and size < 10:
			print(" ", end="")
		elif i / 10 < 1.0 and size >= 10:
			print("  ", end="")
		elif i / 10 >= 1.0 and i / 10 < 10 and size >= 10:
			print(" ", end="")
		if count + 1 == size:
			print(end="\n")
			count = 0
		else:
			print(end=" ")
			count += 1

def is_solvable(puzzle, solution, size):
	# inversion count
	inversions = 0
	for i in range(size * size - 1):
		for j in range(i + 1, size * size):
			if solution.index(puzzle[i]) > solution.index(puzzle[j]):
				inversions += 1
	
	# taxicab dist 
	pos_i = puzzle.index(0)
	y1, x1 = pos_i // size, pos_i % size
	solved_i = solution.index(0)
	y_2, x_2 = q=solved_i // size, solved_i % size
	
	taxicab_dist =  abs(y1 - y_2) + abs(x1 - x_2)
	return taxicab_dist % 2 == inversions % 2
