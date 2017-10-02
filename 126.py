

#Binary search

from __future__ import division

def bin_search(seq, v, l, r):

    if (r-l) == 0:
        return False

    mid = (l+r)//2

    if v == seq[mid]:
        return True

    if v < seq[mid]:
        return bin_search(seq, v , l, mid)

    else:
        return bin_search(seq, v, mid+1, r)

seq = [100,200,300,400,500,600,700]

print bin_search(seq, 400, 0, len(seq))
