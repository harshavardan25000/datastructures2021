class Solution:
    def numIslands(self, grid) -> int:
        count=0
        def traversal(grid,i,j):
            nonlocal count
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0":
                return
            grid[i][j]="0"
            traversal(grid,i+1,j)
            traversal(grid,i-1,j)
            traversal(grid,i,j+1)
            traversal(grid,i,j-1)
            
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    traversal(grid,i,j)
        return count
            
    