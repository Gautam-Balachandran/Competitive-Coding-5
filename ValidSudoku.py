# Time Complexity : O(1), as the size of the board is fixed
# Space Complexity : O(1), as the size of the sets used are fixed
class Solution:
    def __init__(self):
        self.valid1 = True
        self.valid2 = True
        self.valid3 = True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not board or len(board) == 0:
            return False
        self.validateRow(board, 0)
        self.validateCol(board, 0)
        self.validateGrid(board, 0, 0)
        return self.valid1 and self.valid2 and self.valid3

    def validateRow(self, board: list[list[str]], col: int):
        if col >= 9 or not self.valid1:
            return
        seen = set()
        for i in range(9):
            if board[i][col] != '.':
                if board[i][col] in seen:
                    self.valid1 = False
                    return
                else:
                    seen.add(board[i][col])
        
        self.validateRow(board, col + 1)

    def validateCol(self, board: list[list[str]], row: int):
        if row >= 9 or not self.valid1 or not self.valid2:
            return
        
        seen = set()
        for j in range(9):
            if board[row][j] != '.':
                if board[row][j] in seen:
                    self.valid2 = False
                    return
                else:
                    seen.add(board[row][j])
        
        self.validateCol(board, row + 1)

    def validateGrid(self, board: list[list[str]], row: int, col: int):
        if row >= 9 or col >= 9 or not self.valid1 or not self.valid2 or not self.valid3:
            return
        
        seen = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        self.valid3 = False
                        return
                    else:
                        seen.add(board[i][j])
        
        if col == 6:
            col = 0
            row += 3
        else:
            col += 3
        
        self.validateGrid(board, row, col)

# Example 1: Valid Sudoku
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Example 2: Invalid Sudoku (duplicate in row)
board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Example 3: Invalid Sudoku (duplicate in 3x3 grid)
board3 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","6"]
]

solution = Solution()
print(solution.isValidSudoku(board1))  # Output: True
print(solution.isValidSudoku(board2))  # Output: False
print(solution.isValidSudoku(board3))  # Output: False