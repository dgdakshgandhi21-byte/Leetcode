class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row = [False] * rows
        col = [False] * cols

        # Track rows and columns containing 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        # Set elements to 0 based on tracking arrays
        for i in range(rows):
            for j in range(cols):
                if row[i] or col[j]:
                    matrix[i][j] = 0