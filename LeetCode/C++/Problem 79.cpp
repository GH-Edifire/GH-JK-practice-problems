// LeetCode: Problem 79
// Jonathan Kosasih
/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
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

class Solution {
public:
	bool exist(vector<vector<char>>& board, string word) {
		for (int i = 0; i < board.size(); i++) {
			for (int j = 0; j < board[0].size(); j++) {
				if (adjacentSearch(board, word, i, j, 0)) {
					return true;
				}
			}
		}
		return false;
	}
	bool adjacentSearch(vector<vector<char>>& board, const string& word, int i, int j, int index) {
		// found the word
		if (index == word.size()) {
			return true;
		}
		// current location not on board
		if (i < 0 || i > board.size() - 1 || j < 0 || j > board[0].size()-1) {
			return false;
		}
		// current location does not match current letter of word
		if (board[i][j] != word[index]) {
			return false;
		}
		board[i][j] = '*'; // mark as found, to avoid duplicate search
		bool searchCheck = (adjacentSearch(board, word, i - 1, j, index + 1) || // search up
			adjacentSearch(board, word, i, j + 1, index + 1) || // search right
			adjacentSearch(board, word, i + 1, j, index + 1) || // search down
			adjacentSearch(board, word, i, j - 1, index + 1)); // search left
		board[i][j] = word[index]; // change back char after searching
		return searchCheck;
	}
};

int main()
{
    //std::cout << "Hello World!\n";
}