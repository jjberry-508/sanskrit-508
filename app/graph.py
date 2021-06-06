# Adapted from Neelam Yadav https://www.geeksforgeeks.org/find-paths-given-source-destination/

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.return_path = []

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def print_all_paths_util(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            path_copy = []
            for i in path:
                path_copy.append(i)
            self.return_path.append(path_copy)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if not visited[i]:
                    self.print_all_paths_util(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def print_all_paths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.print_all_paths_util(s, d, visited, path)

        return self.return_path

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(1, 3)
    paths = g.print_all_paths(2, 3)