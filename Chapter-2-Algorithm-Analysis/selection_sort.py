def selection_sort(list_s, len_s):
    for i in xrange(len_s):
        min_i = i
        for j in xrange(i+1, len_s):
            if list_s[j] < list_s[min_i]:
                min_i = j
        list_s[i], list_s[min_i] = list_s[min_i], list_s[i]


l = list('SELECTIONSORT')
selection_sort(l, len(l))

assert(''.join(l) == 'CEEILNOORSSTT')
print("Sorted phrase: " + ''.join(l))
