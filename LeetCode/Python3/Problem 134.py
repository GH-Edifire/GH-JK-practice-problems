# LeetCode: Problem 134
# Jonathan Kosasih

#There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
#You begin the journey with an empty tank at one of the gas stations.
#
#Return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
#otherwise return -1.
#
#Note:
#If there exists a solution, it is guaranteed to be unique.
#Both input arrays are non-empty and have the same length.
#Each element in the input arrays is a non-negative integer.
#------------------------------------------------------------------
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if(not gas or not cost or sum(gas) < sum(cost)):
            return -1
        length = len(gas)
        start = 0
        currentGas = 0
        for i in range(length):
            currentGas += gas[i] - cost[i]
            if(currentGas < 0):
                currentGas = 0
                start  = i + 1
        return start      
        
sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(str(sol.canCompleteCircuit(gas, cost)))
gas  = [2,3,4]
cost = [3,4,3]
print(str(sol.canCompleteCircuit(gas, cost)))
gas = [3,1,1]
cost = [1,2,2]
print(str(sol.canCompleteCircuit(gas, cost)))