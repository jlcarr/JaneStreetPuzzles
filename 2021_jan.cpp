// Solution to Jane Street problem 2021 Jan

#include <iostream>
#include <chrono>

#include <limits>

#include <vector>
#include <queue>
#include <set>

/*


*/


double solution(){
	const long n = 4;
	const long N = 4*3*2*1;
	std::vector<double> prob(N, 0.0);
	std::queue<long> next;
	std::set<long> found;

	prob[N-1] = 1.0;
	next.push(N-1);
	found.insert(N-1);

	while(!next.empty()){
		// Obtain current value
		long curr = next.front();
		next.pop();
		double curr_prob = prob[curr];
		//std::cout << curr << " : " << curr_prob << std::endl;
		// Is ending?
		//if (curr % 2 == 0) continue;
		// Compute probability base
		long prob_base = 0;
		long temp = curr;
		for (long radix = 2; radix <= n+1; radix++){
			prob_base += temp % radix;
			temp /= radix;
		}
		//std::cout << "Prob base: " << prob_base << std::endl;
		// Pass on probabilities
		temp = curr;
		long radix_val = 1;
		for (long radix = 2; radix <= n+1; radix++){
			long dig = temp % radix;
			if(dig){
				long next_val = curr - radix_val;
				// Pass along the prob
				prob[next_val] += curr_prob * ((double) dig) / ((double) prob_base);
				// Add to the queue
				if (found.find(next_val) == found.end() && next_val%2){
					found.insert(next_val);
					next.push(next_val);
				}
			}
			temp /= radix;
			radix_val *= radix;
		}
	}

	double result = 0.0;
	for (long curr = 0; curr < N; curr += 2){
		std::cout << curr << " : " << prob[curr] << std::endl;
		std::cout << curr+1 << " : " << prob[curr+1] << std::endl;
		long max_val = 0;
		long temp = curr/2;
		for (long radix = 3; radix <= n+1; radix++){
			long dig = temp % radix;
			long given = radix-1 - dig;
			if(given > max_val){
				max_val = given;
			}
		}
		result += ((double) max_val) * prob[curr];
	}

	//std::cout << std::endl;
	return result;
}

int main(){
	auto t_start = std::chrono::high_resolution_clock::now();
	std::cout.precision(std::numeric_limits<double>::max_digits10);
	std::cout << solution() << std::endl;
	auto t_end = std::chrono::high_resolution_clock::now();
	std::cout << std::chrono::duration<double, std::milli>( t_end - t_start ).count() << std::endl;
	return 0;
}
