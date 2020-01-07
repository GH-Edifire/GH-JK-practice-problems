// LeetCode: Problem 98
// Jonathan Kosasih
/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
using std::stack;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 // modified in-order traversal
class Solution {
public:
	bool isValidBST(TreeNode* root) {
		TreeNode* prev = NULL;
		return validate(root, prev);
	}
	bool validate(TreeNode* node, TreeNode*& prev) {
		if (node == NULL) return true;
		if (!validate(node->left, prev)) return false;
		if (prev != NULL && prev->val >= node->val) return false;
		prev = node;
		return validate(node->right, prev);
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}