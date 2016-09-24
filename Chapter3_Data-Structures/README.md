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