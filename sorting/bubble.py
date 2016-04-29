# 
# Adolfo Jeritson
# Bubble sort implementation
# 2016
#

# inputs: seq: Array of elements
#		  p: first position of the Array
#		  r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def bubblesort(seq, p, r):
    n = p
    N = r+1
    while n != N:
        k = N - 1
        while k != n:
            if seq[k-1] > seq[k]:
               seq[k-1], seq[k] = seq[k], seq[k-1]
            k = k - 1
        n = n + 1