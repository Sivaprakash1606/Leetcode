class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res.add((i, j))  # Store row and column indices as tuples

        for row, col in res:
            # Set the entire row to zero
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

            # Set the entire column to zero
            for i in range(len(matrix)):
                matrix[i][col] = 0