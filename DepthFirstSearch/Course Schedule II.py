# https://leetcode.com/problems/course-schedule-ii/submissions/
# DFS - Method
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        neigh = collections.defaultdict(set)

        for x, y in prerequisites:
            graph[x].add(y)
            neigh[y].add(x)

        result = []

        stack = [i for i in range(numCourses) if not graph[i]]
        while stack:
            node = stack.pop()
            result.append(node)
            for i in neigh[node]:
                graph[i].remove(node)
                if not graph[i]:
                    stack.append(i)
            graph.pop(node)

        return result if len(result) == numCourses else []