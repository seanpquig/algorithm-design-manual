Chapter 5 - Graph Traversal
===

- A graph *G = (V,E)* consists of a set of *vertices* V together with a set *E* of vertex pairs or *edges*.
- The key to using graph algorithms effectively lies in correctly modeling your problem, so you can take advantage of existing algorithms.
	- Becoming familiar with many different graph problems is more important than understanding the details of particular graph algorithms.

###Flavors of Graphs

- *Undirected vs. Directed* - a graph *G = (V,E)* is *undirected* if edge *(x,y)* being in *E* implies *(y,x)* is also in *E*.  Otherwise it is *directed*.
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