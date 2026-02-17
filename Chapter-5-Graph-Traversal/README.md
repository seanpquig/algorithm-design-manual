Chapter 5 - Graph Traversal
===

- A graph `G = (V,E)` consists of a set of *vertices* V together with a set *E* of vertex pairs or *edges*.
- The key to using graph algorithms effectively lies in correctly modeling your problem, so you can take advantage of existing algorithms.
	- Becoming familiar with many different graph problems is more important than understanding the details of particular graph algorithms.

###Flavors of Graphs

- *Undirected vs. Directed* - a graph `G = (V,E)` is *undirected* if edge *(x,y)* being in *E* implies *(y,x)* is also in *E*.  Otherwise it is *directed*.
- *Weighted vs. Unweighted* - Each edge in a *weighted* graph is assigned a numerical value or weight.  In *unweighted* graphs there is no cost distinction.
- *Simple vs. Non-simple* - simple graphs avoid more complex structures like *self-loops* (edges like (x,x)) and *multiedges* in which an edge occurs multiple times in a graph.
- *Sparse vs. Dense* - Sparse graphs have a small fraction of possible vertex pairs have edges.  Dense graphs usually have quadtratic number of edges, while sparse graphs are linear.
- *Cyclic vs. Acyclic* - acyclic graphs do not contain cycles.
	- Trees are acyclic, undirected graphs.
	- DAGs arise naturally in scheduling problems.
		- Toplogical sorting is typcially the first step of any algorithm on a DAG.
- *Embedded vs. Topological* - A graph is *embedded* if the vertices and edges are assigned geometrics positions.
- *Implicit vs. Explicit* - Certain graphs are not explicitly constructed and then traversed, but built as they are used.
- *Labeled vs. Unlabeled* - Each vertex is assigned a unique name or identifier in a *labeled* graph.
	- *isomorphism testing* - determining whether the topological structure for two graphs are identical if we ignore any labels.

#####The Friendship Graph
- Graph where vertices are people and edges indicate two people are fiends.
- Also called *social networks*.
- This graph is sparse
- The *degree* of a vertex is the number of edges adjacent to it.
- *Regular graph* - each vertex has the same degree.

###Data Structures for Graphs
- Two basic graph structures
	1. *Adjacency Matrix*:  Represent G using and n x n matrix M, where M[i,j] = 1 if (i,j) is an edge in G, otherwise 0.
		- fast answers to question "is (i,j) in G?"
		- rapid updates for edge insertion and deletion
		- uses excessive space for graphs with many vertices and relatively few edges.
			- can save space packing multiple bits per word or simulating a triangular matrix on undirected graphs.
			- still inhernetly quadratic on sparse graphs
		- n^2 traversal
	2. *Adjacency Lists*:  more efficiently represent sparse graphs using linked lists to store the neighbors adjacent to each vertex.
		- harder to verify whether a given edge (i,j) is in G, as we now need to search through a list
		- (m + n) memory on small graphs
		- (m + n) traversal

- adjacency lists are the right data structure for most graph applications
- In Python:
	- Edge node:

		```
		class EdgeNode:
    		def __init__(self, y, weight=1, next_node=None):
        		self.y = y
        		self.weight = weight
        		self.next_node = next_node
    	```
    - Graph:

		```
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
    	```
    - Graph initilization function:

    	```
    	def initialize_graph(num_vertices=10, directed=False):
    		graph = Graph([None] * num_vertices, [0] * num_vertices, num_vertices, 0, directed)
    		return graph
    	```
 
###Data Structures for Graphs
- Visiting every edge and vertex in a graph systematically, is perhaps the most fundamental graph problem.
- Key idea behind graph traversal is to mark each vertex when its visited and keep track of what we have not yet completely explored.
	- Each vertex will exist in one of three states:
		- **undiscovered** - the vertex is in its inital, virgin state
		- **discovered** - the vertex has been found, but all incident edges have not been checked yet
		- **processed** - the vertex after we have visited all its incident edges
	- transitions from *undiscovered* => *discovered* => *processsed*

###Breadth-First Search
- In BFS on an undirected graph, we assign a direction to each edge, from the discover *u* to the discovered *v*.
	- we denote *u* to be the parent of *v*.
	- each node has exactly one parent, except for the root.
	- this tree of parents defines the shortest path from the root to every other node in the tree.
		- makes BFS very useful in shortest path problems.
- In Python:
	- these methods were added to the previously implemented `Graph` class

		```
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
		```

	- finding shortest path between `start` and `end` nodes give `parents` array from BFS with `start` as root.

		```
		def find_path(start, end, parents):
    	if (start == end) or (end == -1):
        	print(' ', start)
    	else:
        	find_path(start, parents[end], parents)
        	print(' ', end)
		```