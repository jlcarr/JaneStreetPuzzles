"""Solution to Jane Street's 2021 April puzzle
"""

# Setup problem definition values
bracket = [
	1,
	16,
	8,
	9,
	5,
	12,
	4,
	13,
	6,
	11,
	3,
	14,
	7,
	10,
	2,
	15
]

optimize_index = 14
N = len(bracket)

def compute_probabilities(bracket):
	N = len(bracket)
	probs = [1]*N

	# Continue iterations of bracket pools until you get to the top
	pool_size = 1
	while pool_size < N:
		pool_size *= 2
		# Go over ever pool at this bracket level
		index = 0
		next_probs = [0]*N
		while index < N:
			# Every possible contestant coming from the left side of the bracket
			for left in range(pool_size//2):
				X = bracket[index+left]
				# And every possible contestant coming from the right side of the bracket
				for right in range(pool_size//2,pool_size):
					#print(index,left,right)
					Y = bracket[index+right]
					# Compute the next probabilities
					next_probs[index+left] += probs[index+left] * probs[index+right] * Y / (X + Y)
					next_probs[index+right] += probs[index+left] * probs[index+right] * X / (X + Y)
			index += pool_size
		probs = next_probs
		#print(probs)
	return probs


def optimize_swap(bracket, target=1):
	max_prob = compute_probabilities(bracket)
	max_swappers = ()

	for i in range(N):
		for j in range(i):
			# perform the swap
			temp = bracket[i]
			bracket[i] = bracket[j]
			bracket[j] = temp
		
			new_probs = compute_probabilities(bracket)
			if new_probs[target] > max_prob[target]:
				max_prob = new_probs
				max_swappers = (bracket[i], bracket[j])
		
			# swap back
			temp = bracket[i]
			bracket[i] = bracket[j]
			bracket[j] = temp
	return max_swappers, max_prob


base_probs = compute_probabilities(bracket)
swappers,new_prob = optimize_swap(bracket, target=optimize_index)
improvement = new_prob[optimize_index] - base_probs[optimize_index]

print(f"Baseline probability distribution: {base_probs}")
print(f"New probability distribution: {new_prob}")
print(f"Best seeds to swap: {swappers}")
print(f"Improvement: {improvement}")
