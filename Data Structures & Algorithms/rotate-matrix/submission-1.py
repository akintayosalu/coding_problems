class Solution:
    def buildColumn(self,matrix, colNum, n, values):
        for i, val in enumerate(values):
            matrix[i][colNum] = val

        return



    def rotate(self, matrix: List[List[int]]) -> None:
        #try brute force
        #create new n x n matrix and then first row becomes last column
        n = len(matrix)
        halfHeight = n//2

        #reverse matrix vertically
        # for i in range(halfHeight):
        #     tmp = matrix[i]
        #     matrix[i] = matrix[n-1-i]
        #     matrix[n-1-i] = tmp
        matrix.reverse()

        for i in range(n):
            for j in range(i+1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

