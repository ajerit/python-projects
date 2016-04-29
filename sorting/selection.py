# 
# Adolfo Jeritson
# Selection sort implementation
# 2016
#

# inputs: seq: Array of elements
#		  p: first position of the Array
#		  r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def selectionsort(seq, p, r):
    n = p
    N = r+1
    while n != N:
        a, b = n, N-1
        while a != b:
            if seq[a] <= seq[b]:
               b = b - 1
            else:
               a = a + 1
        seq[n], seq[a] = seq[a], seq[n]
        n = n + 1