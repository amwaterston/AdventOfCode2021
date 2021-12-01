with open('input1.txt') as fp:
	l = [int(x) for x in fp.readlines()]
	print(sum([l[i] < l[i+1] for i in range(len(l)-1)]))
	print(sum([l[i] < l[i+3] for i in range(len(l)-3)]))
	
	
	
		
