from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first create a adj list to track the list of courses that gets unlocked by completigna. prereq
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses # Number of pre-req req by a course
        res = [] # list to get teh order of teh prereq course

        # scan the prereq list and upate the adj and indegree
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        # Do the BFS Approach
        queue = deque()

        # scan the indegree...if emplty list, then that course can be taken
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n) # can be completed as no pre req

        
        while queue:
            node = queue.popleft()
            res.append(node)

            for n in adj[node]:
                indegree[n] -= 1 # trying to dec once the preq has been taken
                if indegree[n] == 0: # that particular course has no pre req
                    queue.append(n)

        return res if len(res) == numCourses else []
