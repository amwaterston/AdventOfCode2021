def pp(dots):
	maxx = max(dots, key = lambda x: x[0])[0] + 1
	maxy = max(dots, key = lambda x: x[1])[1] + 1
	print(f"grid size: {maxx, maxy}")
	grid = [[" "] * maxx for j in range(maxy)]
	for d in dots:
		#print(f"dot: {d}")
		grid[d[1]][d[0]] = "#"
	print("\n".join(["".join(line) for line in grid]))
	
with open('input13.txt') as fp:
	dots, folds = fp.read().split("\n\n")
	dots = [[int(n) for n in line.split(",")] for line in dots.split("\n")]
	
	folds = [[f[11:].split("=")[0], int(f[11:].split("=")[1])] for f in folds.strip().split("\n")]
	#print(dots)
	#print(folds)
	
	for d, n in folds:
		new_dots = []

		if d == 'y':
			xy = 1
		elif d == 'x':
			xy = 0
		#print(f"folding {d}({xy}) along {n}")
		for dot in dots:
			if dot[xy] < n:
				#print(f"dot before fold({n}): {dot}")
				if dot not in new_dots:
					new_dots.append(dot)
			elif dot[xy] > n:
				#print(f"dot after fold({n}): {dot}")
				new_dot = [0, 0]
				new_dot[xy] = n - (dot[xy] - n)
				new_dot[abs(xy-1)] = dot[abs(xy-1)]
				#print(f"new dot: {new_dot}")
				if new_dot not in new_dots:
					new_dots.append(new_dot)
			
		dots = new_dots			
		
	pp(dots)
	print(sorted(dots))
	print(len(dots))
