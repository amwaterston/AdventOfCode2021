with open("input4.txt") as fp:
	numbers, *boxes = fp.read().strip().split("\n\n")
	boxes = [[[int(x) for x in l.split(" ") if x != ''] for l in box.split("\n")] for box in boxes]
	numbers = [int(x) for x in numbers.split(",")]
	e, box = max([(min([max([numbers.index(n) for n in r]) for r in box + list(map(list, zip(*box)))]), box) for box in boxes], key = lambda x: x[0] )
	numbersRemaining = [i for i in [x for l in box for x in l] if i not in numbers[:e+1]]
	print(sum(numbersRemaining) * numbers[e])
