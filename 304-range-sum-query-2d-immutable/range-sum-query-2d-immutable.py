class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix),len(matrix[0])
        self.SumMatrix = [[0]*(cols + 1) for r in range((rows+1))]

        for r in range(rows):
            prefix = 0 
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.SumMatrix[r][c+1]
                self.SumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        r1,r2,c1,c2 =  row1,row2,col1,col2
        r1,r2,c1,c2 = r1+1,r2+1,c1+1,c2+1

        bottomright = self.SumMatrix[r2][c2]
        topleft = self.SumMatrix[r1 - 1][c1 - 1]
        above = self.SumMatrix[r1-1][c2]
        left = self.SumMatrix[r2][c1-1]

        return bottomright - above - left + topleft

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)