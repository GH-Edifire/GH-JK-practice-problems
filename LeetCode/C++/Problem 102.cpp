// LeetCode: Problem 102
// Jonathan Kosasih
/*
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
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
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> answer;
		if (!root) {
			return answer;
		}
		queue<TreeNode*> tracker;
		tracker.push(root);
		while (!tracker.empty()) {
			int n = tracker.size();
			vector<int> currentLevel;
			currentLevel.reserve(n);
			for (int i = 0; i < n; i++) {
				TreeNode* temp = tracker.front();
				tracker.pop();
				if (temp != nullptr) {
					currentLevel.push_back(temp->val);
					tracker.push(temp->left);
					tracker.push(temp->right);
				}
			}
			if (currentLevel.size() > 0) {
				answer.push_back(move(currentLevel));
			}
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}