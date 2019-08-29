# LeetCode: Problem 155
# Jonathan Kosasih

#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.
#------------------------------------------------------------------
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(not self.stack):
            self.stack.append((x, x))
        else:
            newMin = min(self.getMin(), x)
            self.stack.append((x, newMin))

    def pop(self):
        """
        :rtype: None
        """
        x, y = self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        temp = self.stack.pop()
        x, y = temp
        self.stack.append(temp)
        return x
        

    def getMin(self):
        """
        :rtype: int
        """
        temp = self.stack.pop()
        x, y = temp
        self.stack.append(temp)
        return y
    
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.

