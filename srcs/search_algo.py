from srcs.priorityQueue import PriorityQueue
from srcs.utils import print_puzzle
from srcs.node import Node

def new_state(curr_state, i, j):
	tmp = list(curr_state)
	tmp[i], tmp[j] = tmp[j], tmp[i]
	return tuple(tmp)

# UDLR
def moves_list(curr_node, solution, HEURISTIC, G_COST):
	moves = []
	i = curr_node.empty_tile_pos
	size = curr_node.size

	if i - size >= 0:
		state = new_state(curr_node.curr_state, i, i - size)
		up = Node(state, curr_node.curr_state, curr_node.g + G_COST, HEURISTIC(state, solution, size), size, "U")
		moves.append(up)
	if i + size < len(curr_node.curr_state):
		state = new_state(curr_node.curr_state, i, i + size)
		down = Node(state, curr_node.curr_state, curr_node.g + G_COST, HEURISTIC(state, solution, size), size, "D")
		moves.append(down)
	if i % size > 0:
		state = new_state(curr_node.curr_state, i, i - 1)
		left = Node(state, curr_node.curr_state, curr_node.g + G_COST, HEURISTIC(state, solution, size), size, "L")
		moves.append(left)
	if i % size + 1 < size:
		state = new_state(curr_node.curr_state, i, i + 1)
		right = Node(state, curr_node.curr_state, curr_node.g + G_COST, HEURISTIC(state, solution, size), size, "R")
		moves.append(right)
	return moves

def print_path(node, path_list):
	steps = [node.curr_state]
	parent = node.parent

	while parent is not None:
		steps.append(parent)
		parent = path_list[parent]
	steps.reverse()
	for puzzle in steps:
		print_puzzle(puzzle, node.size)
		print("-" * (node.size * 2 + 2))

def A_star(inital_state, solution, size, HEURISTIC, G_COST):
	start = Node(inital_state, None, 0, HEURISTIC(inital_state, solution, size), size)
	queue = PriorityQueue()
	queue.push((start.f, start.g, start))
	open_set = {}
	closed_set = {}

	while queue.heap:
		curr_node = queue.pop()
		if curr_node[2].curr_state == solution:
			print()
			print("SOLVED:")
			print_path(curr_node[2], closed_set)
			print("Complexity in time (Number of states in open_set):", len(open_set))
			print("Complexity in size (Max number of states ever represented in memory at the same time -closed set-):", len(closed_set))
			print("Total Moves:", curr_node[2].g)
			return
		if curr_node[2].curr_state in closed_set:
			continue
		closed_set[curr_node[2].curr_state] = curr_node[2].parent
		t_g = curr_node[2].g + G_COST
		moves = moves_list(curr_node[2], solution, HEURISTIC, G_COST)
		for move in moves:
			if move.curr_state in closed_set:
				continue
			if move.curr_state in open_set:
				move_g, move_h = open_set[move.curr_state]
				move.g = move_g
				move.h = move_h
				if move_g <= t_g:
					continue
			else:
				move_h = move.h
			open_set[move.curr_state] = t_g, move_h
			queue.push((move.f, move.g, move))
