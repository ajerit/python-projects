# 
# Adolfo Jeritson
# Insertion sort implementation
# 2016
#

# inputs: seq: Array of elements
#		  p: first position of the Array
#		  r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def insertionsort(seq, p, r):
    i = p+1
    N = r+1
    while i < N:
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j = j - 1
        i = i + 1