with open("input7.txt") as fp:
	nums = [int(x) for x in fp.read().strip().split(",")]
	print(min([sum([abs(n - p) for p in nums]) for n in nums]))
	print(min([sum([(abs(n - p) * (abs(n-p) + 1))/2 for p in nums]) for n in range(min(nums), max(nums))]))
