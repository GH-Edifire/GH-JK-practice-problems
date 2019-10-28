# LeetCode: Problem 146
# Jonathan Kosasih

#Design and implement a data structure for Least Recently Used (LRU) cache.
#It should support the following operations: get and put.
#
#get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#put(key, value) - Set or insert the value if the key is not already present.
#When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
#The cache is initialized with a positive capacity.
#------------------------------------------------------------------
from collections import deque
class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.order = deque()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key in self.cache):
            value = self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.cache):
            self.order.remove(key)
        self.cache[key] = value
        self.order.append(key)
        if(len(self.cache) > self.capacity):
            oldest = self.order.popleft()
            del self.cache[oldest]
#-------------------------------------------------
# using an OrderedDict, faster
from collections import OrderedDict
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if(key in self.cache):
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if(key in self.cache):
            del self.cache[key]
        self.cache[key] = value
        if(len(self.cache) > self.capacity):
            self.cache.popitem(False)