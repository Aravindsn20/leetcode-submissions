from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Having condition check for the 1st cell and teh last cell
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1 

        
        visit = set() # keep track of teh visited nodes
        queue = deque() # keep track of next set of nodes to process
        queue.append((0,0)) # start form the start of teh cell
        visit.add((0,0)) # start from the start of teh cell
        length = 0 #count the length of the path

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()


                if r == rows - 1 and c == cols - 1:
                    return length

                neighbour = [[1,0], [-1,0], [0,1], [0,-1]] # all themovements - d,u,r,l
                for dr, dc in neighbour:
                    nr, nc = r + dr, c + dc # new col, and new rows

                    #check of teh outbound conditions
                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                    
                    queue.append((nr,nc))
                    visit.add((nr,nc))
                    
            length += 1
        
        return -1


        
