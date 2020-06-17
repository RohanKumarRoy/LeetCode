'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

#code written by Rohan Kumar Roy

class Solution:
    def isconnected(self, board, i, j):
        board[i][j] = '1'
        if i > 0 and board[i - 1][j] == 'O':
            self.isconnected(board, i-1, j)
        if j > 0 and board[i][j - 1] == 'O':
            self.isconnected(board, i, j - 1)
        if i < len(board) - 1 and board[i + 1][j] == 'O':
            self.isconnected(board, i + 1, j)
        if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
            self.isconnected(board, i, j + 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []
        
        for i in range(0, len(board)):
            if board[i][0] == 'O':
                self.isconnected(board, i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                self.isconnected(board, i, len(board[0]) - 1)
        
        for j in range(1, len(board[0]) - 1):
            if board[0][j] == 'O':
                self.isconnected(board, 0, j)
            if board[len(board) - 1][j] == 'O':
                self.isconnected(board, len(board) - 1, j)
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
        