with open("input6.txt") as fp:
	fish = [int(x) for x in fp.read().strip().split(",")]
	fish_gens = [fish.count(i) for i in range(9)]
	for d in range(256):
		new_fish = fish_gens.pop(0)
		fish_gens[6] += new_fish
		fish_gens.append(new_fish)
	print(sum(fish_gens))
