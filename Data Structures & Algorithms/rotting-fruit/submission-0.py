from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #1. Scan the Grid, add all the rotten oranges to teh queue. get the count of teh fresh oranges
        #2. BFS - pop the oranges from the queue...and do BFS on all the rotten spots / oranges at each elevl / miunute 
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0

        for r in range((rows)):
            for c in range((cols)):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        #BFS
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbour = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in neighbour:
                    nr, nc = r + dr, c + dc

                    # outbound checks
                    if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1
            

             
        