// LeetCode: Problem 103
// Jonathan Kosasih
/*
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
	vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
		vector<vector<int>> answer;
		if (!root) {
			return answer;
		}
		deque<TreeNode*> tracker;
		tracker.push_back(root);
		int reverseFlag = 0;
		while (!tracker.empty()) {
			int n = tracker.size();
			vector<int> currentLevel;
			currentLevel.reserve(n);
			for (int i = 0; i < n; i++) {
				TreeNode* temp = tracker.front();
				tracker.pop_front();
				if (temp != nullptr) {
					currentLevel.push_back(temp->val);
					tracker.push_back(temp->left);
					tracker.push_back(temp->right);
				}
			}
			if (reverseFlag & 1) {
				reverse(currentLevel.begin(), currentLevel.end());
			}
			if (currentLevel.size() > 0) {
				answer.push_back(move(currentLevel));
			}
			reverseFlag++;
		}
		return answer;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}