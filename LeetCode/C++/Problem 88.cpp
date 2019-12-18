// LeetCode: Problem 88
// Jonathan Kosasih
/*
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
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
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		int index1 = m - 1;
		int index2 = n - 1;
		int currentIndex = m + n - 1;
		while (index1 >= 0 && index2 >= 0) {
			if (nums1[index1] > nums2[index2]) {
				nums1[currentIndex] = nums1[index1];
				index1 -= 1;
			}
			else {
				nums1[currentIndex] = nums2[index2];
				index2 -= 1;
			}
			currentIndex -= 1;
		}
		if (index2 >= 0) {
			for (int i = 0; i <= index2; i++) {
				nums1[i] = nums2[i];
			}
		}
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}