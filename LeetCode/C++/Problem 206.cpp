// LeetCode: Problem 206
// Jonathan Kosasih
/*
Reverse a singly linked list.
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
	// iterative
	ListNode* reverseList(ListNode* head) {
		ListNode* scout = head;
		ListNode* current = NULL;
		while (scout) {
			ListNode* temp = scout->next;
			scout->next = current;
			current = scout;
			scout = temp;
		}
		return current;
	}
	// recursive
	ListNode* reverseListRecursive(ListNode* head) {
		if (head == NULL || head->next == NULL) {
			return head;
		}
		ListNode* scout = reverseListRecursive(head->next);
		head->next->next = head;
		head->next = NULL;
		return scout;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}