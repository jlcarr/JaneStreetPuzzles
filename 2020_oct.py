import itertools
import math
import numpy as np
from scipy.special import factorial
import random

# Setup
n = 4


def gen_perm(distrib, row, col, n):
	# This condition is true if all completed valid arrangement has been constructed
	if col == n:
		# Consider we conly have counts of candies given to children
		# We must therefore consider all arrangements of candies given to children
		# All possible permutations of distinct candies for each child is: math.factorial(n)**n
		# However same candies are not distinct: therefore each candy type needs its permutation divided out: np.prod(factorial(distrib,exact=True))
		instances = math.factorial(n)**n // np.prod(factorial(distrib,exact=True))
		# Consider printing for debugging
		#print(distrib) if random.randrange(100) == 0 else None
		#print(instances)
		return instances
	if row == col:
		# We are ensuring max candies are chosen first with row=-1, therefore of we get to row==col, we pass through
		# More explanation on this logic in the loop below
		new_distrib = np.copy(distrib)
		if row+1 < n:
			return gen_perm(new_distrib,row+1,col,n)
		elif np.sum(new_distrib[:,col]) == n:
			return gen_perm(new_distrib,-1, col+1,n)
		return 0
	ans = 0
	for i in range(n):
		# First check if we're dealing with the child with the max of a given candy type first
		if row == -1:
			# If so, ensure we're allowd to give 'i' more copies of their candy to them
			if np.sum(distrib[col,:]) + i <= n:
				# If so continue the search by distributing remaing copies of this candy to the other children
				new_distrib = np.copy(distrib)
				new_distrib[col,col] += i
				ans += gen_perm(new_distrib,row+1,col,n)
		# If giving more 'i' copies of the 'col' candy to the 'row' child won't break the strictly less-than condition
		# and we wouldn't be giving more than the number of compies we have of this candy
		elif distrib[row,col]+i < distrib[col,col] and np.sum(distrib[row,:]) + i <= n:
			new_distrib = np.copy(distrib)
			new_distrib[row,col] += i
			# If we still have children to dole out this candy to:
			if row+1 < n:
				ans += gen_perm(new_distrib,row+1,col,n)
			# otherwise if we've exactly distributed all copies of this candy out
			elif np.sum(new_distrib[:,col]) == n:
				# Onto the next candy type, starting with the max-child
				ans += gen_perm(new_distrib,-1, col+1,n)
	return ans


# initiate all diagonal kids as having the most of 1 type of candy
count = gen_perm(2*np.eye(n, dtype=np.int), -1, 0, n)


# Add in all the possible permutations of types of candy for a kid to have the most of
count = count * math.factorial(n)
# For the total configurations possible, it's all permutations of candy, but the candies are non-distinct: all perms of candies of a given types are divided out
total = math.factorial(n*n)//math.factorial(n)**n


print(f"Raw count = {count} / {total}")
print(f"In lowest terms = {count//math.gcd(count,total)} / {total//math.gcd(count,total)}")
print(f"In decimal = {count/total}")
