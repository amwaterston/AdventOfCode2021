def mostCommon(numbers, position, default):
	s = sum(list(zip(*numbers))[position])
	m = len(numbers) / 2
	if s > m:
		return int(1 == default)
	elif s < m:
		return int(0 == default)
	else:
		return default

def filter(numbers, position, bit):
	return [x for x in numbers if x[position] == bit]
	
def filterMostCommon(numbers, bit, default):
	return filter(numbers, bit, mostCommon(numbers, bit, default))

def findValue(numbers, default):
	sl = numbers[:]
	for i in range(len(sl[0])):
		sl = filterMostCommon(sl, i, default)
		if len(sl) == 1:
			return sl[0]

def binListToInt(bits):
	return int("".join([str(x) for x in bits]), base = 2)
	
with open("input3.txt") as fp:
	ls = [[int(d) for d in l.strip()] for l in fp.readlines()]
	gamma = [int(sum(l) > len(ls) / 2) for l in zip(*ls)]
	epsilon = [int(not bool(g)) for g in gamma]
	print(f"answer 1: {binListToInt(gamma) * binListToInt(epsilon)}")
	
	ox = binListToInt(findValue(ls, 1))
	co2 = binListToInt(findValue(ls, 0))
	print(f"answer 2: {ox * co2}")
