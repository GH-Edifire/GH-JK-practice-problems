// LeetCode: Problem 26
// Jonathan Kosasih
/*
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
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
	int removeDuplicates(vector<int>& nums) {
		int i = 0;
		for (int n : nums)
			if (!i || n > nums[i - 1])
				nums[i++] = n;
		return i;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}