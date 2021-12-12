def traverse(caves, current, visited, done_a_double):
	count = 0
	for p in caves[current]:
		if (current.islower()):
			new_visited = visited + [current]
		else:
			new_visited = visited + []
		if p == "end":
			count += 1
		elif p not in visited:
			count += traverse(caves, p, new_visited, done_a_double)
		elif p in visited and not done_a_double and p != "start":
			count += traverse(caves, p, new_visited, True)
	return count
			
with open("input12.txt") as fp:
	caves = {}
	for start, end in [line.strip().split("-") for line in fp.readlines()]:
		if start in caves:
			caves[start].append(end)
		else:
			caves[start] = [end]
		if end in caves:
			caves[end].append(start)
		else:
			caves[end] = [start]
	
	print(traverse(caves, "start", [], True))
	print(traverse(caves, "start", [], False))
