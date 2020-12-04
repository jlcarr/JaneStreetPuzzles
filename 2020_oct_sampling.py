import itertools
import numpy as np
import random
import time
t_start = time.time()

n = 5
n_samples = 10000

# Generate the intital permutations
candy_lineup = list(range(n))*n
# Choose either a sampling of the permutations, or all of them uniquely
#perms = [[np.array(perm[i:i+n]) for i in range(0,n*n,n)] for perm in itertools.permutations(v)]
perms = [[np.array(perm[i:i+n]) for i in range(0,n*n,n)] for perm in [random.sample(candy_lineup, n*n) for sample in range(n_samples)]]


#for i in perms:
#	print(i)

#print(len(perms))


# Reformulate as as a matrix of candies and children on each axis, and the elements being counts of candy type owned by child
perms = [np.array([np.bincount(child, minlength=n) for child in perm]) for perm in perms]


# Define a function that ensures the max value in a 1-d array is unique (ensures only 1 child has the most of 1 candy!)
check_max_unique = lambda arr: np.bincount(arr)[np.max(arr)] == 1
#for i,perm in enumerate(perms):
	#print(f"Permutation {i}")
	#print(perm)
	#print(f"Is valid: {np.all(np.apply_along_axis(check_max_unique, 0, i)) and np.max(np.bincount(np.argmax(i,axis=0))) == 1)}")


# to check is a configuration is valid we must ensure for each candy only 1 child has that max value
# However we must also ensure that those with the max values of candies are unique: no kid has 2 copies of 2 types of candies while all others have 1 copy of those 2 types
valid = [perm for perm in perms if np.all(np.apply_along_axis(check_max_unique, 0, perm)) and np.max(np.bincount(np.argmax(perm,axis=0))) == 1]


#for i in valid:
#	print(i)

print(f"{len(valid)} / {len(perms)}")
print(len(valid)/len(perms))
print(time.time()-t_start)
