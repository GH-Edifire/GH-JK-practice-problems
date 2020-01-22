// LeetCode: Problem 127
// Jonathan Kosasih
/*
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
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

class Solution {
public:
	int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
		unordered_set<string> dict(wordList.begin(), wordList.end()), head, tail, * phead, * ptail;
		if (dict.find(endWord) == dict.end()) {
			return 0;
		}
		head.insert(beginWord);
		tail.insert(endWord);
		int ladder = 2;
		while (!head.empty() && !tail.empty()) {
			if (head.size() < tail.size()) {
				phead = &head;
				ptail = &tail;
			}
			else {
				phead = &tail;
				ptail = &head;
			}
			unordered_set<string> temp;
			for (auto it = phead->begin(); it != phead->end(); it++) {
				string word = *it;
				for (int i = 0; i < word.size(); i++) {
					char t = word[i];
					for (int j = 0; j < 26; j++) {
						word[i] = 'a' + j;
						if (ptail->find(word) != ptail->end()) {
							return ladder;
						}
						if (dict.find(word) != dict.end()) {
							temp.insert(word);
							dict.erase(word);
						}
					}
					word[i] = t;
				}
			}
			ladder++;
			phead->swap(temp);
		}
		return 0;
	}
};
int main()
{
    //std::cout << "Hello World!\n";
}