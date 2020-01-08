// LeetCode: Problem 101
// Jonathan Kosasih
/*
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
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
using std::vector;
using std::map;
using std::unordered_map;
using std::set;
using std::stack;
using std::queue;

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
	bool isSymmetric(TreeNode* root) {
		if (!root) return true;
		queue<TreeNode*> check;

		check.push(root->left);
		check.push(root->right);

		while (!check.empty()) {
			TreeNode* node1 = check.front();
			check.pop();
			TreeNode* node2 = check.front();
			check.pop();
			if (!node1 && node2) return false;
			if (!node2 && node1) return false;
			if (node1 && node2) {
				if (node1->val != node2->val) return false;
				check.push(node1->left);
				check.push(node2->right);

				check.push(node1->right);
				check.push(node2->left);
			}
		}
		return true;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}