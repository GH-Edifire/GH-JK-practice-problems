// LeetCode: Problem 141
// Jonathan Kosasih
/*
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
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
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	bool hasCycle(ListNode* head) {
		ListNode* current = head;
		ListNode* scout = head;
		while (scout) {
			scout = scout->next;
			if (!scout) {
				return false;
			}
			else {
				scout = scout->next;
			}
			if (scout == current) {
				return true;
			}
			current = current->next;
		}
		return false;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}