// LeetCode: Problem 108
// Jonathan Kosasih
/*
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;
using std::deque;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	TreeNode* sortedArrayToBST(vector<int>& nums) {
		if (nums.size() == 0) {
			return NULL;
		}
		if (nums.size() == 1) {
			return new TreeNode(nums[0]);
		}
		int mid = nums.size() / 2;
		TreeNode* root = new TreeNode(nums[mid]);
		vector<int> leftSide(nums.begin(), nums.begin() + mid);
		vector<int> rightSide(nums.begin() + mid + 1, nums.end());
		root->left = sortedArrayToBST(leftSide);
		root->right = sortedArrayToBST(rightSide);
		return root;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}