class Node():
	def __init__(self, curr_state, parent, g, h, size, mov="root"):
		self.curr_state = curr_state
		self.parent = parent
		self.h = h
		self.g = g
		self.empty_tile_pos = curr_state.index(0)
		self.f = self.g + self.h
		self.size = size
		self.mov = mov

	def __str__(self):
		ret = ""
		ret += "Node data: " + self.mov + "\n"
		ret += "-matrix:         " + str(self.curr_state) + "\n"
		ret += "-parent:         " + str(self.parent) + "\n"
		ret += "-size:           " + str(self.size) + "\n"
		ret += "-h:              " +  str(self.h) + "\n"
		ret += "-g:              " + str(self.g) + "\n"
		ret += "-f:              " + str(self.f) + "\n"
		ret += "-empty_tile_pos: " + str(self.empty_tile_pos)
		return ret
	
	def __lt__(self, nxt):
		return self.f < nxt.f
