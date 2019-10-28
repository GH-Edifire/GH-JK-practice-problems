# LeetCode: Problem 130
# Jonathan Kosasih

#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
#A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#Example:
#X X X X
#X O O X
#X X O X
#X O X X
#
#After running your function, the board should be:
#X X X X
#X X X X
#X X X X
#X O X X
#
#Explanation:
#Surrounded regions shouldn’t be on the border,
#which means that any 'O' on the border of the board are not flipped to 'X'.
#Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
#Two cells are connected if they are adjacent cells connected horizontally or vertically.
#------------------------------------------------------------------
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if(not board):
            return
        
        borderOs = False
        stack = []
        # scan borders for O's
        # top row
        for i in range(len(board[0])):
            if(board[0][i] == "O"):
                borderOs = True
                stack.append((0,i))
        # right column
        for i in range(1,len(board)):
            if(board[i][len(board[0])-1] == "O"):
                borderOs = True
                stack.append((i,len(board[0])-1))
        # bottom row
        for i in range(len(board[0])-2, -1, -1):
            if(board[len(board)-1][i] == "O"):
                borderOs = True
                stack.append((len(board)-1,i))
        # left column
        for i in range(len(board)-1, 0, -1):
            if(board[i][0] == "O"):
                borderOs = True
                stack.append((i,0))
        
        if(borderOs):
            while(stack):
                row, col = stack.pop(0)
                board[row][col] = "S"
                # check neighbors
                # check above
                if((row-1) > 0 and board[row-1][col] == "O"):
                    stack.append((row-1,col))
                # check right
                if((col+1) < len(board[row]) and board[row][col+1] == "O"):
                    stack.append((row,col+1))
                # check below
                if((row+1) < len(board) and board[row+1][col] == "O"):
                    stack.append((row+1,col))
                # check left
                if((col-1) > 0 and board[row][col-1] == "O"):
                    stack.append((row,col-1))
                    
        # change O's to X and marked S to O's 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                    
                if(board[i][j] == "S"):
                    board[i][j] = "O"
                    
        self.printBoard(board)
    
    def printBoard(self, board):
        for i in range(len(board)):
            print(board[i])
        
sol = Solution()
board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
print(str(sol.solve(board)))
