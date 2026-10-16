class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSubSquare(board: List[List[str]], centerI: int, centerJ: int) -> bool:
            nums = []
            myset = set()

            for i in range(centerI - 1, centerI + 2):
                for j in range(centerJ - 1, centerJ + 2):
                    if board[i][j] != '.':
                        nums.append(board[i][j])
                        myset.add(board[i][j])
            if len(nums) != len(myset):
                return False
            return True            
        
        def checkRow(board: List[List[str]], index: int) -> bool:
            myset = set()
            for i in range(9):
                if board[index][i] != '.':
                    if board[index][i] in myset:
                        return False
                    myset.add(board[index][i])
            return True
        
        def checkCol(board: List[List[str]], index: int) -> bool:
            myset = set()
            for i in range(9):
                if board[i][index] != '.':
                    if board[i][index] in myset:
                        return False
                    myset.add(board[i][index])
            return True
        
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                if not checkSubSquare(board, i, j):
                    return False
        for i in range(9):
            if not checkRow(board, i):
                return False
            if not checkCol(board, i):
                return False
        return True
        