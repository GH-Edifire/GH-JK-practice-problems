// LeetCode: Problem 146
// Jonathan Kosasih
/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
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

class LRUCache {
public:
	LRUCache(int capacity) : myCap(capacity) {

	}

	int get(int key) {
		if (myMap.find(key) == myMap.end())
			return -1;
		auto it = myMap[key];
		const int val = it->second;
		myList.erase(it);
		myMap[key] = myList.insert(myList.begin(), make_pair(key, val));
		return val;
	}

	void put(int key, int value) {
		if (myMap.find(key) != myMap.end()) {
			myList.erase(myMap[key]);
			myMap.erase(key);
		}
		if (myMap.size() >= myCap) {
			int keyToBeRemoved = myList.rbegin()->first;
			myList.pop_back();
			myMap.erase(keyToBeRemoved);
		}
		myMap[key] = myList.insert(myList.begin(), make_pair(key, value));
	}
private:
	list<pair<int, int> > myList;
	unordered_map<int, list<pair<int, int> >::iterator > myMap;
	const int myCap;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
int main()
{
    //std::cout << "Hello World!\n";
}