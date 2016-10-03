from __future__ import print_function
import random


class EdgeNode:
    def __init__(self, y, weight=1, next_node=None):
        self.y = y
        self.weight = weight
        self.next_node = next_node


class Graph:
    def __init__(self, edges, degrees, num_vertices, num_edges, directed=False):
        self.edges = edges
        self.degrees = degrees
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.directed = directed

    def show(self):
        for i in xrange(self.num_vertices):
            print('Vertex:', i)
            print('  Edges:', end='')
            edge = self.edges[i]
            while edge:
                print('', edge.y, end='')
                edge = edge.next_node
            print('')

    def insert_edge(self, x, y, directed=False):
        edge = EdgeNode(y, next_node=self.edges[x])
        self.edges[x] = edge
        self.degrees[x] += 1

        if not directed:
            self.insert_edge(y, x, True)
        else:
            self.num_edges += 1

    def bfs(self, start):
        """
        Breadth-First Search implmentation
        start: index of root vertex to being searching from
        return: parents array to be used for finding shortest paths
        """
        processed = [False] * self.num_vertices
        discovered = [False] * self.num_vertices
        parents = [-1] * self.num_vertices

        # queue of vertices to process
        queue = [start]
        discovered[start] = True

        while len(queue) > 0:
            v = queue.pop()
            self.process_vertex_early(v)
            processed[v] = True
            edge = self.edges[v]
            while edge:
                y = edge.y
                if (not processed[y]) or self.directed:
                    self.process_edge(v, y)
                if not discovered[y]:
                    queue.insert(0, y)
                    discovered[y] = True
                    parents[y] = v
                edge = edge.next_node

            self.process_vertex_late(v)

        return parents

    @staticmethod
    def process_vertex_early(v):
        pass

    @staticmethod
    def process_vertex_late(v):
        print('  processed vertex', v)

    @staticmethod
    def process_edge(x, y):
        print('  processed edge ({}, {})'.format(x, y))


def initialize_graph(num_vertices=10, directed=False):
    graph = Graph([None] * num_vertices, [0] * num_vertices, num_vertices, 0, directed)
    return graph


def find_path(start, end, parents):
    if (start == end) or (end == -1):
        print(' ', start)
    else:
        find_path(start, parents[end], parents)
        print(' ', end)


# Setup a graph to run algorithms
graph = initialize_graph()
# Randomly generate edges
for i in xrange(graph.num_vertices):
    x = int(random.random() * graph.num_vertices)
    y = int(random.random() * graph.num_vertices)
    if x != y:
        graph.insert_edge(x, y)

print('# vertices', graph.num_vertices)
print('# edges:', graph.num_edges)
graph.show()

# Run BFS
print('\nRunning Breadth-First Search...')
parents = graph.bfs(0)

print('\nShortest path between node 0 and node 9')
find_path(0, 9, parents)
