// LeetCode: Problem 19
// Jonathan Kosasih
/*
Given a linked list, remove the n-th node from the end of list and return its head.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>
#include <algorithm> 
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
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode* fast = head;
		ListNode* slow = head;
		for (int i = 0; i < n; i++) {
			fast = fast->next;
		}
		if (fast == NULL) {
			return head->next;
		}
		while (fast->next != NULL) {
			fast = fast->next;
			slow = slow->next;
		}
		slow->next = slow->next->next;
		return head;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}