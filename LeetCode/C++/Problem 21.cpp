// LeetCode: Problem 21
// Jonathan Kosasih
/*
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (l1 == NULL) { return l2; }
		if (l2 == NULL) { return l1; }
		ListNode* head = NULL;
		if (l1->val < l2->val) {
			head = l1;
			l1 = l1->next;
		}
		else {
			head = l2;
			l2 = l2->next;
		}
		ListNode* builder = head;
		while (l1 && l2) {
			if (l1->val <= l2->val) {
				builder->next = l1;
				l1 = l1->next;
			}
			else {
				builder->next = l2;
				l2 = l2->next;
			}
			builder = builder->next;
		}
		if (l1) {
			builder->next = l1;
		}
		else {
			builder->next = l2;
		}
		return head;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}