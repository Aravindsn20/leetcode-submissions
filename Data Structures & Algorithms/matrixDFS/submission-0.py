class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            #Check for outbound condition for bloackage
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r, c) in visit:
                return 0
            
            #check to reach teh final cell of the grid
            elif r == rows - 1 and c == cols - 1:
                return 1

            # udpate teh visited node
            visit.add((r, c))
            #count the no of paths from top left to bottom right
            count = 0
            count += dfs(r - 1, c) # move top
            count += dfs(r + 1, c) # move bottom
            count += dfs(r, c - 1) # move left
            count += dfs(r, c + 1) # move right

            visit.remove((r, c))

            return count
        return dfs(0,0)
