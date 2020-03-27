// LeetCode: Problem 234
// Jonathan Kosasih
/*
Given a singly linked list, determine if it is a palindrome.
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
	bool isPalindrome(ListNode* head) {
		if (head == nullptr || head->next == nullptr) return true;

		// Find middle & reverse 2nd half of the list
		ListNode* reversed2ndHalf = reverseList(findMiddle(head));

		// Verify palindrome property
		while (reversed2ndHalf != nullptr && head)
		{
			if (reversed2ndHalf->val != head->val)
				return false;

			reversed2ndHalf = reversed2ndHalf->next;
			head = head->next;
		}

		return true;
	}

private:
	ListNode* findMiddle(ListNode* head)
	{
		if (head == nullptr || head->next == nullptr) return head;

		ListNode* slow = head; ListNode* fast = head;
		while (fast != nullptr && fast->next != nullptr)
		{
			slow = slow->next;
			fast = fast->next->next;
		}

		// If we have an odd number of elements skip over the middle element
		if (fast != nullptr) slow = slow->next;

		return slow;
	}

	ListNode* reverseList(ListNode* head)
	{
		if (head == nullptr || head->next == nullptr) return head;

		ListNode* prev = nullptr;
		while (head != nullptr)
		{
			ListNode* next = head->next;
			head->next = prev;
			prev = head;
			head = next;
		}

		return prev;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}