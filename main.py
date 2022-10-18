import sys
from srcs.parser import parse_file, parse
from srcs.utils import print_puzzle, is_solvable
from srcs.search_algo import A_star
from srcs.heuristics import hammingDistance, manhattanDistance, euclideanDistance, uniform, HEURISTICS
from srcs.solution_generator import SOLUTIONS

def main():
	try:
		args = parse()
		parsed_file = parse_file(args.file)
		puzzle = parsed_file[0]
		size = parsed_file[1]
		solution = SOLUTIONS[args.solution](size)
		if args.uniform == True:
			HEURISTIC = uniform
		else:
			HEURISTIC = HEURISTICS[args.algorithm]
		if args.greedy == True:
			G_COST = 0
		else:
			G_COST = 1
		print("Initial state:")
		print_puzzle(puzzle, size)
		print()
		print("Heuristics initial values:")
		print("-Manhatan Distance:", manhattanDistance(puzzle, solution, size))
		print("-Hamming Distance:", hammingDistance(puzzle, solution, size))
		print("-Euclidean Distance:", euclideanDistance(puzzle, solution, size))
		print()
		print("Expected solution:")
		print_puzzle(solution, size)
		if is_solvable(puzzle, solution, size) == True:
			A_star(puzzle, solution, size, HEURISTIC, G_COST)
		else:
			print()
			exit("This puzzle is not solvable")
	except Exception as e:
		print("Error:", e)

if __name__ == "__main__":
	main()