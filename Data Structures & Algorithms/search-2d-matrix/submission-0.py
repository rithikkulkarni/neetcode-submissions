class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix) * len(matrix[0])
        arr = []
        for subarr in matrix:
            arr += subarr
        
        l = 0
        r = length - 1
        m = (l + r) // 2

        while l <= r:
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
        return False