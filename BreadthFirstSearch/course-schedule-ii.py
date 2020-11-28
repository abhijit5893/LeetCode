#https://leetcode.com/problems/course-schedule-ii/
from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        path = []
        while len(q):
            item = q.popleft()
            path.append(item)
            for v in graph[item]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return path[::-1] if sum(indegree) ==0 else []
