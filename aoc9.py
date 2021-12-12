def getNumber(numbers, x, y):
	if x < 0 or y < 0 or y > len(numbers) - 1 or x > len(numbers[0]) - 1:
		return 10
	else:
		return numbers[y][x]
		
def lowerThanAllNeighbours(numbers, x, y):
	d = [(0, 1), (0,-1), (1, 0), (-1, 0)]
	v = getNumber(numbers, x, y)
	return all([v < getNumber(numbers, x + dx, y + dy) for dx, dy in d])

def getNeighbourCoords(numbers, x, y):
	d = [(0, 1), (0,-1), (1, 0), (-1, 0)]
	return [(x + dx, y + dy) for dx, dy in d]
	
def getNonNineNeighbours(numbers, x, y):
	n = getNeighbourCoords(numbers, x, y)
	return [p for p in n if getNumber(numbers, p[0], p[1]) < 9]
	
with open("input9_bobby.txt") as fp:
	grid = [[int(l) for l in list(line.strip())] for line in fp.readlines()]
	lowPoints = [(x, y) for x in range(len(grid[0])) for y in range(len(grid)) if lowerThanAllNeighbours(grid, x, y)]
	print(sum([getNumber(grid, x, y) + 1 for x, y in lowPoints]))
	
	basin_product = []
	
	for x, y in lowPoints:
		to_visit = [(x, y)]
		c = 0
		while len(to_visit) > 0:
			c += 1
			nx, ny = to_visit.pop()
			grid[ny][nx] = 11
			neighbours = getNonNineNeighbours(grid, nx, ny)
			#print(f"{nx}, {ny} neighbours: {neighbours}")
			to_visit = list(set(to_visit).union(set(neighbours)))
			#print(f"{to_visit}")
		print(c)
		basin_product.append((c, (x, y)))
	basin_product.sort(key = lambda x : x[0])
	
	print(f"number of basins: {len(basin_product)}")
	print(basin_product[-3:])
	print(basin_product[-3][0] * basin_product[-2][0] * basin_product[-1][0])
