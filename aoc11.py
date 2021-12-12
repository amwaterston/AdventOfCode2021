class Grid:
	def __init__(self, grid):
		self.grid = grid
		self.flashed = set([])
		
	def get(self, x, y):
		return self.grid[y][x]
		
	def inc(self, x, y):
		if (x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid)):
			self.grid[y][x] += 1

	def set(self, x, y, v):
		if (x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid)):
			self.grid[y][x] = v		
			
	def flashocto(self, x, y):
		for dx, dy in [(-1,-1), (0,-1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
			self.inc(x + dx, y + dy)
		self.flashed.add((x, y))
	
	def reset(self):
		self.grid = [[c if c <= 9 else 0 for c in line] for line in self.grid]
		
	def energy(self):
		self.grid = [[c + 1 for c in line] for line in self.grid]
	
	def flash(self):
		count = 0
		for y in range(len(self.grid)):
			for x in range(len(self.grid[0])):
				if (self.get(x, y) > 9 and not (x, y) in self.flashed):
					self.flashocto(x, y)
					count += 1
		return count
		
	def flashuntilnomoreflashes(self):
		self.flashed = set([])
		total_flashes = 0
		while True:
			flashes = self.flash()
			total_flashes += flashes
			if flashes == 0: break
		return total_flashes
		
	def to_s(self):
		return "\n".join(["\t".join([str(c) for c in line]) for line in self.grid])
		
	def octocount(self):
		return len(grid) * len(grid[0])
			
	
with open("input11.txt") as fp:
	grid = [[int(c) for c in list(line.strip())] for line in fp.readlines()]
	g = Grid(grid)
	print(g.to_s())
	total_flashes = 0
	for i in range(1000):
		g.energy()
		flashes = g.flashuntilnomoreflashes()
		if (flashes == g.octocount()):
			print(f"Synchroflash on step {i + 1}")
			print(g.to_s())
			break
		total_flashes += flashes
			
		g.reset()
		
	print(total_flashes)
