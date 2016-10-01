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


def initialize_graph(num_vertices=10, directed=False):
    graph = Graph([None] * num_vertices, [0] * num_vertices, num_vertices, 0, directed)
    return graph


graph = initialize_graph()
# Randomly generate edges
for i in xrange(graph.num_vertices):
    x = int(random.random() * graph.num_vertices)
    y = int(random.random() * graph.num_vertices)
    graph.insert_edge(x, y)

print('# vertices', graph.num_vertices)
print('# edges:', graph.num_edges)
graph.show()
