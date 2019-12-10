// LeetCode: Problem 66
// Jonathan Kosasih
/*
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;

class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		digits[digits.size() - 1] += 1;
		for (int i = digits.size() - 1; i >= 0; i--) {
			if (digits[i] > 9 && i != 0) {
				digits[i] = 0;
				digits[i - 1] += 1;
			}
			else if (digits[i] > 9 && i == 0) {
				digits[i] = 0;
				digits.insert(digits.begin(), 1);
				break;
			}
		}
		return digits;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}