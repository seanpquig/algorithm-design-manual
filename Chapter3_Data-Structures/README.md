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