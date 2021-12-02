with open('input2.txt') as fp:
	ls = [l.split() for l in fp.readlines()]
	f = sum([int(n) for o, n in ls if o == "forward"])
	d = sum([int(n) for o, n in ls if o == "down"])
	u = sum([int(n) for o, n in ls if o == "up"])
	print((d - u) * f)
	
	aim = x = y =0
	for o, n in ls:
		if o == 'down':
				aim += int(n)
		elif o == 'up':
				aim -= int(n)
		elif o == 'forward':
				x += int(n)
				y += aim * int(n)
	print(x * y)				
