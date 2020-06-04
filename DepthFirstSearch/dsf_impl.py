from collections import defaultdict

'''
Steps
1. Create a dictionary to store the graph
2. Build the graph -> adjacency list
3. Initialize a array for visited
4. For all the unvisited visit it and go deeper recursively
5. Return the traversal

Complexity - O(V+E)
'''
# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end='')

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # The function  to do DFS traversal. It used recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Call the recursive helper function to pting DFS traversal
        self.DFSUtil(v, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS(2)
