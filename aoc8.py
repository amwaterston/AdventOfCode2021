with open("input8a.txt") as fp:
	uniques = [2, 4, 3, 7]	
	lines = [[digit for digit in line.strip().split(" | ")] for line in fp.readlines()]
	sum = 0
	for digits, number in lines:
		digits = [sorted(d) for d in digits.split(" ")]
		#print(digits)
		numbers = {}
		numbers[1] = [d for d in digits if len(d) == 2][0]
		digits.remove(numbers[1])
		numbers[4] = [d for d in digits if len(d) == 4][0]
		digits.remove(numbers[4])
		numbers[7] = [d for d in digits if len(d) == 3][0]
		digits.remove(numbers[7])
		numbers[8] = [d for d in digits if len(d) == 7][0]
		digits.remove(numbers[8])
		numbers[9] = [d for d in digits if all(l in d for l in numbers[4])][0]
		digits.remove(numbers[9])
		numbers[0] = [d for d in digits if len(d) == 6 and all(l in d for l in numbers[1])][0]
		digits.remove(numbers[0])
		numbers[6] = [d for d in digits if len(d) == 6][0]
		digits.remove(numbers[6])
		numbers[3] = [d for d in digits if all(l in d for l in numbers[1])][0]
		digits.remove(numbers[3])
		numbers[5] = [d for d in digits if len(set(numbers[9]).difference(set(d))) == 1][0]
		digits.remove(numbers[5])
		numbers[2] = digits.pop()
		
		letters = {}
		letters["".join(numbers[0])] = 0		
		letters["".join(numbers[1])] = 1	
		letters["".join(numbers[2])] = 2		
		letters["".join(numbers[3])] = 3
		letters["".join(numbers[4])] = 4
		letters["".join(numbers[5])] = 5
		letters["".join(numbers[6])] = 6
		letters["".join(numbers[7])] = 7
		letters["".join(numbers[8])] = 8
		letters["".join(numbers[9])] = 9
		
		print(letters)
		sum += int("".join([str(letters["".join(sorted(num))]) for num in number.split(" ")]))
		
	print(sum)
