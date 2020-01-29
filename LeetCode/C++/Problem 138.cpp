// LeetCode: Problem 138
// Jonathan Kosasih
/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
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

/*
// Definition for a Node.
class Node {
public:
	int val;
	Node* next;
	Node* random;

	Node(int _val) {
		val = _val;
		next = NULL;
		random = NULL;
	}
};
*/
// memoization / DP
// create new objects if not already saved in our memo
class Solution {
public:
	unordered_map<Node*, Node*>mp;
	Node* copyRandomList(Node* head)
	{
		if (!head) return NULL;
		if (mp[head] != NULL) return mp[head];
		mp[head] = new Node(head->val);
		mp[head]->next = copyRandomList(head->next);
		mp[head]->random = copyRandomList(head->random);
		return mp[head];
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}