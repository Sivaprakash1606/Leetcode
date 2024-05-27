class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=set()
        c=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for k in range(len(matrix)):
            for l in range(len(matrix[0])):
                if k in r or l in c:
                    matrix[k][l] = 0