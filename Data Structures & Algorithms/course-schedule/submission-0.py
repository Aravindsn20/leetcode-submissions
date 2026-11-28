from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can create a graph / adj list to track the pre req of teh courses
        adj = {i: [] for i in range(numCourses)} # To track the number of courses that can be uncloked by completign a course
        indegree = [0] * numCourses # Number of pre-req required to complete the course
        # loop through the pre-re list and update for indegree nd adj
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        #Declare a queue...check if any coure can be completed...like having no prereq. 

        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n) # can be completed as no pre req

        taken = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                taken += 1 # updating the count of taken course

                for n in adj[node]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)
                

        return taken == numCourses