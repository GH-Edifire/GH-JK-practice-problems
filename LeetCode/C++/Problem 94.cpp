// LeetCode: Problem 94
// Jonathan Kosasih
/*
Given a binary tree, return the inorder traversal of its nodes' values.
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
class Solution {
public:
	vector<int> inorderTraversal(TreeNode* root) {
		vector<int> answer;
		if (root == NULL) {
			return answer;
		}
		this->inorderHelper(root, answer);
		return answer;
	}

	void inorderHelper(TreeNode* root, vector<int>& answer) {
		if (root->left) {
			this->inorderHelper(root->left, answer);
		}
		answer.push_back(root->val);
		if (root->right) {
			this->inorderHelper(root->right, answer);
		}
	}

	vector<int> inorderTraversalIter(TreeNode* root) {
		vector<int> answer;
		if (root == NULL) {
			return answer;
		}
		stack<TreeNode*> stack;
		while (!stack.empty() || root) {
			while (root) {
				stack.push(root);
				root = root->left;
			}
			root = stack.top();
			stack.pop();
			answer.push_back(root->val);
			root = root->right;
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}