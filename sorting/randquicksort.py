# 
# Adolfo Jeritson
# Random Quicksort implementation
# 2016
#

import random

def rand_partition(seq, p, r):
    i = random.randint(p, r)
    seq[i], seq[r] = seq[r], seq[i]
    x = seq[r]
    i = p - 1
    for j in range(p, r):
        if seq[j]<=x:
            i=i+1
            seq[i],seq[j]=seq[j],seq[i]
    seq[i+1],seq[r] = seq[r], seq[i+1]
    return i+1

# inputs: seq: Array of elements
#         p: first position of the Array
#         r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def rand_quicksort(seq, p, r):
    if p < r:
        q = rand_partition(seq, p, r)
        rand_quicksort(seq, p, q-1)
        rand_quicksort(seq, q+1, r)