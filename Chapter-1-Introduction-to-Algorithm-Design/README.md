Chapter 1 - Introduction to Algorithm Design
===

###Insertion Sort
in Python:

    def insertion_sort(list_s, len_s):
        for i in xrange(1, len_s):
            j = i
            while j > 0 and (list_s[j] < list_s[j-1]):
                list_s[j-1], list_s[j] = list_s[j], list_s[j-1]
                j -= 1


###Expressing Algorithms
- Three common forms of algoritmhmic notation:

	1. English
	2. Pseudocode
	3. A true programming language

- The heart of any algorithm is an idea.  If that idea is not clearly expressed, you are using too low-levle a notation.

###Demonstrating Incorrectness
- Good counter examples exhibit:
	- Verifiability
	- Simplicity
- Techniques for finding counter-examples
	- Think small
	- Think exhaustively
	- Hunt for the weakness
	- Go for a tie
	- Seek extremes

###Combinatorial Objects
- Common structures
	- **Permutations**: arrangements or orderings of items
	- **Subsets**: selections from a set of items.  Order does not matter.
	- **Trees**: represent hierarchical relationships
	- **Graphs**: represent relationships between arbitrary pairs of objects.  Web or network-like
	- **Polygons**: regions in geometric space
	- **Strings**: sequences of characters or patterns
