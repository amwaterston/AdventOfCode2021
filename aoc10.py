bracket_points = {
	")" : 3,
	"]" : 57,
	"}" : 1197,
	">" : 25137
}
incomplete_bracket_points = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4,
}
opens = [ "(", "[", "{", "<"]
closes = [ ")", "]", "}", ">"]
corruption_points = 0
all_incomplete_points = []
with open("input10.txt") as fp:
	lines = [list(line.strip()) for line in fp.readlines()]
	for line in lines:
		brackets = []
		incomplete_points = 0
		corrupt_line = False
		for c in line:
			if c in opens:
				brackets.append(c)
			elif c in closes:
				last = brackets.pop()
				if (opens.index(last) != closes.index(c)):
					corruption_points += bracket_points[c]
					corrupt_line = True
					break
		if not corrupt_line and len(brackets) != 0:
			for b in brackets[::-1]:
				incomplete_points *= 5
				incomplete_points += incomplete_bracket_points[closes[opens.index(b)]]
			all_incomplete_points.append(incomplete_points)
				

print(f"part 1: {corruption_points}")
print(f"part 2: {sorted(all_incomplete_points)[int(len(all_incomplete_points) / 2)]}")
