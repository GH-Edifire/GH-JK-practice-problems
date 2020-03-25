// LeetCode: Problem 230
// Jonathan Kosasih
/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
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
	// recursive, inorder traversal
	int kthSmallest(TreeNode* root, int k) {
		vector<int> vSmallest;
		Smallestkth(root, k, vSmallest);
		return vSmallest[k - 1];
	}
	void Smallestkth(TreeNode* root, int k, vector<int>& vSmallest) {
		if (root->left) Smallestkth(root->left, k, vSmallest);
		vSmallest.push_back(root->val);
		if (root->right) Smallestkth(root->right, k, vSmallest);
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}