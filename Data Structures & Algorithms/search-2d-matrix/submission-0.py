class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        rows = len(matrix)
        cols = len(matrix[0])
        hi = (rows*cols) - 1

        while (lo <= hi):
            mid = lo + (hi-lo)//2

            mid_row = mid//cols
            mid_cols = mid%cols
            mid_num = matrix[mid_row][mid_cols]

            if mid_num == target:
                return True
            elif mid_num > target:
                hi = mid - 1
            elif mid_num < target:
                lo = mid + 1

        return False