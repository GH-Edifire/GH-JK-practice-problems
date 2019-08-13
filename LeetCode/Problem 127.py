# LeetCode: Problem 127
# Jonathan Kosasih

#Given two words (beginWord and endWord), and a dictionary's word list,
#find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#Only one letter can be changed at a time.
#Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
#Note:
#Return 0 if there is no such transformation sequence.
#All words have the same length.
#All words contain only lowercase alphabetic characters.
#You may assume no duplicates in the word list.
#You may assume beginWord and endWord are non-empty and are not the same.
#------------------------------------------------------------------
from string import ascii_lowercase
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)
        if(endWord not in words):
            return 0
        if(len(beginWord) != len(wordList[0])):
            return 0
        
        # bi-directional BFS
        # we know endWord is in our wordList, so mark it as seen
        seen = {endWord}
        beginQueue = []
        begin = [beginWord]
        end = [endWord]
        count = 1
        while(begin and end):
            # search lowest amount of options first
            if(len(begin) > len(end)):
                begin, end = end, begin
                
            nextSet = set()
            for word in begin:
                # generate all word/char neighbors, and compare
                for neighbor in self.getNeighbors(word):
                    # neighbor can be found in our end list
                    if(neighbor in end):
                        return count+1
                    # if a neighbor is in our word list and we haven't seen it yet,
                    # mark it as seen and check it next time
                    if(neighbor in words and neighbor not in seen):
                        seen.add(neighbor)
                        nextSet.add(neighbor)
            begin = nextSet
            count += 1
                
        return 0

    # generates words with a 1 character difference
    def getNeighbors(self, word):
        neighbors = set()
        for i in range(len(word)):
            for char in ascii_lowercase:
                nextWord = word[:i] + char + word[i+1:]
                neighbors.add(nextWord)
        return neighbors
        
sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(str(sol.ladderLength(beginWord, endWord, wordList)))
