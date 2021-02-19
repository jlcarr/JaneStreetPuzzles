# Given k (mutually indistinct) figurines of type k, k-1 figurines of type k-1, etc... and n draws, 
# how many ways distinct are there to assign these n draws to the total k*(k+1)/2 figurines?

# This function is interesting to compute and shall be used to help monitor the progress of our computation

# We use memoization to compute our problem more quickly
prev = dict()
def F(n,k):
	# If already memorize, we can return the answer right away
	if (n,k) in prev:
		return prev[(n,k)]
	# If the number of draws is exactly equal to the number of remaining figurines they we must assign all draws to all remaining figures.
	if n == k*(k+1)/2:
		return 1
	# If we have more draws than figurines we there are no valid allocations
	if n > k*(k+1)/2:
		return 0
	v = sum([F(i,k-1) for i in range(max(1,n-k),n+1)]) + int(k>=n)
	prev[(n,k)] = v
	return v

K = 12
N_MAX = K*(K+1)//2

tot = sum([F(i,K) for i in range(N_MAX+1)])
print(f"Total number of states: {tot}")
max_step =  max([F(i,K) for i in range(N_MAX+1)])
print(f"Biggest step size of: {max_step}")


# Use this to help estimate progress 
L = 38
sofar = sum([F(i,K) for i in range(N_MAX+1) if i > L])

print(f"Progress at step {L} is: {sofar/tot}")
