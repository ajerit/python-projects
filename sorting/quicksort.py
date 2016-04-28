# 
# Adolfo Jeritson
# Quicksort implementation
# 2015
#

def partition(seq, p, r):
    x = seq[r]
    i = p - 1
    
    for j in range(p, r):
        if seq[j] <= x:
            i = i + 1
            seq[i], seq[j] = seq[j], seq[i]
    seq[i+1], seq[r] = seq[r], seq[i+1]
    
    return i + 1
    
# inputs: seq: Array of elements
#		  p: first position of the Array
#		  r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def quicksort(seq, p, r):
    if p < r:
        q = partition(seq, p, r)
        quicksort(seq, p, q-1)
        quicksort(seq, q+1, r)