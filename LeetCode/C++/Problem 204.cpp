// LeetCode: Problem 204
// Jonathan Kosasih
/*
Count the number of prime numbers less than a non-negative number, n.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <algorithm> 
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;
using std::accumulate;

class Solution {
public:
	// sieve of eratosthenes
	int countPrimes(int n) {
		if (n < 3) {
			return 0;
		}
		vector<bool> primes(n, true);
		primes[0] = false;
		primes[1] = false;
		for (int i = 0; i < sqrt(n); i++) {
			if (primes[i]) {
				for (int j = i * i; j < n; j += i) {
					primes[j] = false;
				}
			}
		}
		return count(primes.begin(), primes.end(), true);
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}