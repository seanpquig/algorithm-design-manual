def findmatch(p, t):
    m = len(p)
    n = len(t)

    for i in xrange(n-m+1):
        j = 0
        while (j < m) and (t[i+j] == p[j]):
            j += 1
            if j == m:
                return i

    return -1


assert(findmatch('abba', 'aababba') == 3)
