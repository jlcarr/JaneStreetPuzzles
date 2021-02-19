import random

N = 3
samples = 1000000

max_val_avg = 0
for sample in range(samples):
	drawn = []
	bag = [fig for fig_set in range(1,N+1) for fig in [fig_set]*fig_set]
	#print(bag)

	while True:
		i = random.randrange(len(bag))
		selection = bag.pop(i)
		#print(i, selection)
		if selection == 1:
			break
		drawn.append(selection)

	#print(drawn)
	if len(drawn) == 0:	
		continue

	counts = [0]*(N-1)
	for fig in drawn:
		counts[fig-2] += 1

	i,count = max(enumerate(counts), key=lambda element: element[1])
	max_val_avg += count
	#print(count)

max_val_avg /= samples

print(max_val_avg)
