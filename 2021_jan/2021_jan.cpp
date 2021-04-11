// Solution to Jane Street problem 2021 Jan
//g++ -std=c++0x 2021_jan.cpp -O3

#include <iostream>
#include <chrono>

#include <limits>

#include <map>
#include <queue>

/*


*/


double solution(){
	//const long long n = 12;
	const long long n = 2;
	//const long long N = 13LL*12LL*11LL*10LL*9LL*8LL*7LL*6LL*5LL*4LL*3LL*2LL*1LL;
	const long long N = 3*2*1;
	std::map<long long,double> prob;
	std::queue<long long> next;

	prob[N-1] = 1.0;
	next.push(N-1);

	double result = 0.0;

	long long base_target = n*(n+1)/2;

	while(!next.empty()){
		// Obtain current value
		long long curr = next.front();
		next.pop();
		double curr_prob = prob[curr];
		prob.erase(curr);
		//std::cout << curr << " : " << curr_prob << std::endl;
		//if (curr % 2 == 0) continue;
		// Compute probability base
		long long prob_base = 0;
		long long max_given = 0;
		long long temp = curr;
		for (long radix = 2; radix <= n+1; radix++){
			// which figurine are we looking at?
			long long fig = temp % radix;
			// determine the max figs given
			long long given =  radix-1 - fig;
			if(radix >= 3 && given > max_given) max_given = given;
			prob_base += fig;
			temp /= radix;
		}
		double prob_base_double = (double) prob_base;
		//std::cout << "Prob base: " << prob_base << std::endl;
		if (prob_base <= base_target){
			std::cout << "Prob base: " << prob_base << std::endl;
			base_target--;
		}
		// Pass on probabilities
		temp = curr;
		long long radix_val = 1;
		for (long long radix = 2; radix <= n+1 && temp; radix++){
			long long dig = temp % radix;
			if(dig){
				long long next_val = curr - radix_val;
				// If the value is an end state update the return value
				if (next_val%2 == 0){
					result += ((double) max_given) * curr_prob / prob_base_double;
				}
				// otherwise make sure it's in the queue and probability is passed on
				else if(prob.find(next_val) == prob.end()) {
					next.push(next_val);
					prob[next_val] = curr_prob * ((double) dig) / prob_base_double;
				}
				else{
					prob[next_val] += curr_prob * ((double) dig) / prob_base_double;
				}
			}
			temp /= radix;
			radix_val *= radix;
		}
	}

	std::cout << result << std::endl;
	std::cout << std::endl;
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
