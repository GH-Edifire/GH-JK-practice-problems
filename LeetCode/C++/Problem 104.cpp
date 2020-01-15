// LeetCode: Problem 104
// Jonathan Kosasih
/*
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
	int maxDepth(TreeNode* root) {
		if (!root) {
			return 0;
		}
		int depth = 0;
		queue<TreeNode*> q;
		q.push(root);
		while (!q.empty()) {
			vector<int> currentLevel;
			queue<TreeNode*> newQ;
			int size = q.size();
			for (int i = 0; i < size; i++) {
				if (q.front()) {
					currentLevel.push_back(q.front()->val);
					newQ.push(q.front()->left);
					newQ.push(q.front()->right);
				}
				q.pop();
			}
			q = newQ;
			if (!currentLevel.empty()) {
				depth += 1;
			}
			currentLevel.clear();
		}
		return depth;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}