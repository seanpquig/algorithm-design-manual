Chapter 3 - Data Structures
===

- 3 fundamental abstract data types
	1. Containers
	2. Dictionaries
	3. Priority Queues

###Contiguous vs Linked data structures

- *Contiguous*: composed of single slabs of memory (arrays, marticies, heaps, and hash tables)
- *Linked*: composed of distinct chunks of memory bound together by pointers (lists, trees, and graph adjacency lists)

- **Arrays**
	- constant-time access via an index
	- space efficiency
	- memory locality
	- fixed size
	- *Dyanmic arrays* allow size to increase, but certain queries can result in O(n) operations when elements need to be copied during array re-sizing.

- **Linked Structures**
	- Much of the space in linked structures must be devoted to pointers linking items.
	- **\*p** to denote the item pointed to by pointer **p**.
	- **&x** to denote the the address/pointer of/to variable **x**.
	- linked list in C:

		```
		typedef struct list {
			item_type item;       /* data item */
			struct list *next;    /* point to successor */
		}
		```
	- overflow on linked structures can never occur unless memory is exhausted.
	- insertions and deletions are easier.
	- with large records, it's easier/faster to move pointers than items.
	- random access of items is not as efficient.
	- poorer memory locality and cache performance.

###Stacks and Queues
- *Container* denotes a data structure that permits storage and retrieval *independent of content*.  By contrast, dictionaries retrieve based on key values or content.
- Containers are distinguished by the retrieval orders they support.
- 2 container types:
	- *Stacks* - retrieval by last-in, first-out (LIFO)
		- LIFO tends to happen during execution of recursive algorithms.
	- *Queues* - retrievla by first-in, first-out (FIFO)
		- minimized max time spent waiting
		- generally trickier to implement than stacks
	- both can be implemented with arrays or linked lists.

###Dictionaries
- The *dictionary* permits access to data items by content.
- The fastest data structure to support both operation A and B may not be the fastest structure to support either A or B.

###Binary Search Trees
- Binary search trees give us a balance of relatively fast search and flexible updates.
- *Rooted binary tree* recursivley defineds as being either
	1. Empty
	2. consisting of node called root, together with two rooted binary trees calle dteh left and right subtrees
- For any binary tree of *n* nodes, and any set of *n* keys, there is *exactly* one labeling that makes it a binary search tree.
- Binary tree nodes have *left* and *right* pointer fields, and an optional *parent* pointer.
- In Python:
	- Tree structure

		```
		class BinaryTree:
    		def __init__(self, item=None, left=None, right=None):
        		self.item = item
        		self.left = left
        		self.right = right
        ```
    - Searching tree:
    
    	```
    	def search(self, x):
        	if not self.item:
            	return None

        	if self.item == x:
            	return self
        	if x < self.item:
            	if self.left:
                	return self.left.search(x)
        	elif self.right:
            	return self.right.search(x)

        	return None
    	```
    
    - Finding min or max element:
    
    	```
    	def minimum(self):
        	if not self.item:
            	return None

        	if not self.left:
            	return self
        	else:
            	return self.left.minimum()

    	def maximum(self):
        	if not self.item:
            	return None

        	if not self.right:
            	return self
        	else:
            	return self.right.maximum()
    	```
    	
    - Traversing Tree
  
    	```
    	def traverse(self, func=None):
        	if self.left:
            	self.left.traverse(func)
        	if func:
            	func(self.item)
        	if self.right:
            	self.right.traverse(func)
    	```
    
    - Inserting Item:
   
   		```
    	def insert(self, x):
        	if not self.item:
            	self = BinaryTree(x)

        	if x < self.item:
            	if self.left:
                	self.left.insert(x)
            	else:
                	self.left = BinaryTree(x)
        	else:
            	if self.right:
                	self.right.insert(x)
            	else:
                	self.right = BinaryTree(x)
    	```

- Using a binary tree, all 3 dictionary opertions (search, insert, delete) take `O(h)` or `O(log(n))` time.  Assuming the tree is perfectly balanced.
- In practice, tree heights can range from lg(n) to n.
- *Randomization* can ofte provide simple algorithms with a high probablitly of good performance.

#####Balanced Search Trees
- Balanced trees have insertion/deletion procedures that adjust the tree to keep its maximum height logarithmic.
- Red-black trees and Splay trees are implementations of balanced tree data structures.

###Priority Queue
- Priority queues support 3 operations:
	- *Insert(Q, x)* - Insert item x with key k, in the queue.
	- *Find-Min(Q), Find-Max(Q)* - return pointer to item with smallest or largest key in the queue.
	- *Delete-Min(Q), Delete-Max(Q)* - Remve the item from the queue whose key is the min or max.

###Hashing and Strings
- Hash tables are a very practical way to maintain a dictionary.
	- they exploit the fact that looking an item up in an array takes constant time when you have its index.
- Hash function maps keys to a large integer.
	- Let *⍺* be the size of the alphabet on which a string *S* is written
	- Let *char(c)* be a function that maps each symbol of the alphabet to a unique integer from 0 to *⍺* - 1
	- `H(S) = Σ(i=0...|S|-1) ⍺^(|S| - (i+1)) * char(s_i))`
		- treats characters of the string as "digits" in a base-⍺ number system.
- These massive integers from a hash function need to be reduced to fit in the number of slots in a hash table (m).
	- `H(S) mod m`
- Uniform hash table distribution is aided by choosing *m* to be a large prime not too close to `2^i -1`.
- *Chaining* is the easiest approach to resolving hash collisions.
	- Represent Hash table as an array of m linked lists.
		- *ith* list will contain all items that hash to *i*
	- devotes considerable memory to pointers
- *Open addressing* is another approach for resolving collisions.
	- on insertion, if desired position is not empty, item is inserted in next open spot in the table (*sequential probing*).
	- deletion in this scheme can get ugly, since removing an element might break a chain of insertions.
	- *n* must be at most *m*
- Pragmatically, a hash table is often the best data structure to maintain a dictionary.

#####Efficient String Matching via Hashing
- The primary data structure representing strings is an array of characters.
- Substring pattern matching
	- Simplest algorithm from prior chapter runs in O(nm) where n and m are lenths of text and sub-string pattern.
	- Rabin-Karp algorithm
		- linear *expected-time*
		- Hash the pattern string *p*, and the *len(p)* substring starting from position i.
		- Some algebra on hash functions of consecutive substrings leads us to:

			```
			H(S,j+1) = ⍺(H(S,j) - ⍺^(m-1)*char(s_j)) + char(s_j+m)
			```

		- Assuming minimal hash collisions, we get a very fast linear algorithm.

#####Duplicate Detection Via Hashing
- Key idea of hasing is to represent a large object (key, string) using a single number that can be manipulated in constant time.
- Examples of problems with nice hashing solutions:
	- Checking if a document exists in a large corpus
	- Detecting plagirism by hashing all substrings of a given length in a corpus of docs
	- Detecting file changes.

- Worst-case bounds in hashing are usually dismal, but a proper hash function will avoid those.
- Hashing is fundamental in randomized algorithms.
	- can yield linear expected-time algos for `O(nlog(n))` or `O(n^2)` problems.

###Specialized Data Structures
- Basic data structures so far all represent an unstructured set of items so as to facilitate retrieval operations.
- Some more specialized data structures:
	- *String data structures* - Suffix trees/arrays can preprocess strings to make pattern matching operations faster.
	- *Geometric data structures* - spatial structures like kd-trees organize points and regions by geometric location to support fast search.
	- *Graph data structures* - typically represented using adjacency matrices or adjacency lists.
	- *Set data structures* - typically represented with dictionaries.  Bit vectors or union-find structures are alternatives.

###Chapter Notes
- optimizing hash table performance is surprisingly complicated for a conceptually simple data structure.
	- the importance of short runs in open addressing has let to more complicated schemes than sequential probing for collision resolution.