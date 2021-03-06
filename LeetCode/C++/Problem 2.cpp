// LeetCode: Problem 2
// Jonathan Kosasih
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/
//-------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
using std::vector;
using std::map;
using std::unordered_map;


//Definition for singly-linked list.
struct ListNode {
	int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		int carry = 0;
		ListNode newHead(0);
		ListNode* t = &newHead;
		while (carry || l1 || l2) {
			carry += (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
			t->next = new ListNode(carry % 10);
			t = t->next;
			carry /= 10;
			if (l1) {
				l1 = l1->next;
			}
			if (l2) {
				l2 = l2->next;
			}
		}
		return newHead.next;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}