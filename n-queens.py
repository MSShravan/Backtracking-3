# Time Complexity : O(n!)
# Space Complexity : O(n^2)  
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Check upper left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # Check upper right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row, board, res):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1, board, res)
                    board[row][col] = '.'

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board, res)
        return res
        