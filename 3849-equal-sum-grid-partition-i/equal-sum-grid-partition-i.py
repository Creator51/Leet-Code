class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row,col = len(grid),len(grid[0])

        row_sum = [0] * row
        col_sum = [0] * col

        total =0 

        for i in range(row):
            for j in range(col):
                #total Sum
                total += grid[i][j]
                #row_sum
                row_sum[i] += grid[i][j]
                #col_sum
                col_sum[j] += grid[i][j]

        if total % 2 != 0:
            return False

        #Horizontal_cut
        upper=0

        for i in range(row - 1):
            upper += row_sum[i]
            if upper == total - upper:
                return True

        #horizontal Cut
        left=0
        for i in range(col - 1):
            left += col_sum[i]
            if left == total - left:
                return True

        return False


            
        