import random as rnd
import time
import code


def bin_search(x, search_list, l_idx):
    """ 
    Return index of x in search_list.  If x doesn't exist, return None.
    l_idx keeps track of the relative index to the  original call list.
    """
    if not search_list:
        return

    len_l = len(search_list)
    idx = int(len_l / 2)
    item = search_list[idx]

    if item > x:
        return bin_search(x, search_list[:idx], l_idx)
    elif item < x:
        return bin_search(x, search_list[idx+1:], l_idx + idx + 1)
    elif item == x:
        return idx + l_idx


def sort_big(m, n):
    intersect = []
    n = sorted(n)

    # Confirm if each element of m is in n
    for i in m:
        match_idx =  bin_search(i, n, 0)
        if match_idx:
            intersect.append(n[match_idx])

    return intersect


def sort_small(m, n):
    intersect = []
    m = sorted(m)

    # Confirm if each element of n is in m
    for i in n:
        match_idx =  bin_search(i, m, 0)
        if match_idx:
            intersect.append(m[match_idx])

    return intersect


def iterate_through(m, n):
    intersect = []
    m = sorted(m)
    n = sorted(n)

    m_idx = n_idx = 0
    while m_idx < len(m) and n_idx < len(n):
        m_val, n_val = m[m_idx], n[n_idx]

        if m_val == n_val:
            intersect.append(m_val)
            m_idx, n_idx = m_idx + 1, n_idx + 1
        elif m_val > n_val:
            n_idx = n_idx + 1
        elif m_val < n_val:
            m_idx = m_idx + 1

    return intersect



# Generate lists
m_len = 10
n_len = 1000
m = list(set([int(rnd.uniform(0, n_len*5)) for i in xrange(m_len*2)]))[:m_len]
n = list(set([int(rnd.uniform(0, n_len*5)) for i in xrange(n_len*2)]))[:n_len]

# Time function runtime
t0 = time.time()

code.interact(local=locals())
intersect_sb = sort_big(m, n)
code.interact(local=locals())
intersect_ss = sort_small(m, n)
code.interact(local=locals())
intersect_it = iterate_through(m, n)

t1 = time.time()

print 'final set:  ', intersect_sb
print 'final set:  ', intersect_ss
print 'final set:  ', intersect_it
print 'runtime:  ', t1 - t0


