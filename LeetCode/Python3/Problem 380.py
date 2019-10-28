# LeetCode: Problem 380
# Jonathan Kosasih

#Design a data structure that supports all following operations in average O(1) time.
#
#insert(val): Inserts an item val to the set if not already present.
#remove(val): Removes an item val from the set if present.
#getRandom: Returns a random element from current set of elements.
#Each element must have the same probability of being returned.
#------------------------------------------------------------------
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val not in self.randomSet):
            self.randomSet[val] = 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        temp = self.randomSet.pop(val, False)
        return True if temp != False else temp
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randomArray = []
        i = 0
        for key in self.randomSet:
            randomArray.append(key)
        return randomArray[random.randint(0,len(randomArray)-1)]

# FASTER ALT
#import random
#class RandomizedSet:
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.length = 0
#        self.idxToVal = {}
#        self.valToIdx = {}
#        
#
#    def insert(self, val: int) -> bool:
#        """
#        Inserts a value to the set. Returns true if the set did not already contain the specified element.
#        """
#        if val in self.valToIdx:
#            return False
#        
#        self.idxToVal[self.length] = val
#        self.valToIdx[val] = self.length
#        self.length += 1
#        return True
#
#    def remove(self, val: int) -> bool:
#        """
#        Removes a value from the set. Returns true if the set contained the specified element.
#        """
#        
#        if val not in self.valToIdx:
#            return False
#        
#        index = self.valToIdx[val]
#        
#        del self.valToIdx[val]
#        del self.idxToVal[index]
#        if index == self.length - 1:
#            self.length -= 1
#            return True
#        else:
#            newVal = self.idxToVal[self.length-1]
#            self.valToIdx[newVal] = index
#            self.idxToVal[index] = newVal
#            self.length -= 1
#            return True
#        
#
#    def getRandom(self) -> int:
#        """
#        Get a random element from the set.
#        """
#        # print(self.idxToVal, self.length)
#        randIdx = random.randint(0, self.length-1)
#        return self.idxToVal[randIdx]
            
sol = RandomizedSet()
sol.insert(1)
sol.insert(2)
print(str(sol.getRandom()))
sol.remove(2)
sol.remove(3)
print(str(sol.getRandom()))
