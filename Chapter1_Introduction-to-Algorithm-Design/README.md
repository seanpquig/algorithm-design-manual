Chapter 1 - Introduction to Algorithm Design
===

###Insertion Sort
in Python

	def insertion_sort(list_s, len_s):
    for i in xrange(1, len_s):
        j = i
        while j > 0 and (list_s[j] < list_s[j-1]):
            list_s[j-1], list_s[j] = list_s[j], list_s[j-1]
            j -= 1