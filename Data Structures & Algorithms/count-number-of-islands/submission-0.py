class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visit = set() #to track teh visited nodes
        island = 0
        
        def dfs(r,c):
            #check for outbound conditions
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == '0' or (r,c) in visit:
                return

            #check if its in part of the cufrrent island
            visit.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r,c)
                    island += 1
        return island