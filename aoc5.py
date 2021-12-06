with open("input5.txt") as fp:
	vh_lines = [line for line in [[[int(n) for n in v.split(",")] for v in l.split(" -> ")] for l in fp.readlines()]]
	grid = [[0] * 1000 for j in range(1000)]
	for line in vh_lines:
		#print(f"point 1: {line[0]}")
		#print(f"point 2: {line[1]}")
		xoffset = line[1][0] - line[0][0]
		yoffset = line[1][1] - line[0][1]
		xstep = 0
		ystep = 0
		if xoffset != 0:
			xstep = int(xoffset / abs(xoffset))
		if yoffset != 0:
			ystep = int(yoffset / abs(yoffset))
		for i in range(0, max(abs(xoffset), abs(yoffset)) + 1):
			#print(f"x: {line[0][0]} + ({xstep} * {i}): {line[0][0] + (xstep * i)}")
			#print(f"y: {line[0][1]} + ({ystep} * {i}): {line[0][1] + (ystep * i)}")
			grid[line[0][0] + (xstep * i)][line[0][1] + (ystep * i)] += 1
	#print(grid)
	print(len([point for line in grid for point in line if point > 1]))
