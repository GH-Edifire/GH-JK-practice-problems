// LeetCode: Problem 160
// Jonathan Kosasih
/*
Write a program to find the node at which the intersection of two singly linked lists begins.
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
	ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
		if (!headA || !headB) {
			return NULL;
		}
		ListNode* pathOne = headA;
		int pathOneLength = 0;
		ListNode* pathTwo = headB;
		int pathTwoLength = 0;
		while (pathOne->next) {
			pathOne = pathOne->next;
			pathOneLength += 1;
		}
		while (pathTwo->next) {
			pathTwo = pathTwo->next;
			pathTwoLength += 1;
		}
		if (pathOne != pathTwo) {
			return NULL;
		}

		pathOne = headA;
		pathTwo = headB;

		if (pathOneLength > pathTwoLength) {
			int i = 0;
			while (i < (pathOneLength - pathTwoLength)) {
				pathOne = pathOne->next;
				i++;
				if (pathOne == pathTwo) {
					return pathOne;
				}
			}
		}
		else if (pathOneLength < pathTwoLength) {
			int i = 0;
			while (i < (pathTwoLength - pathOneLength)) {
				pathTwo = pathTwo->next;
				i++;
				if (pathTwo == pathOne) {
					return pathTwo;
				}
			}
		}
		while (pathOne != pathTwo) {
			pathOne = pathOne->next;
			pathTwo = pathTwo->next;
		}
		return pathOne;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}