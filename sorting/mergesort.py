#
# Adolfo Jeritson
# Merge sort implementation
# 2015

def merge(seq,p,q,r):
    n = q-p+1
    m = r-q
    L, R = [], []

    for i in range(0, n):
        L.append(seq[p+i])
    for j in range(0, m):
        R.append(seq[q+j+1])

    L.append(10000000)
    R.append(10000000)

    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            seq[k] = L[i]
            i = i + 1
        else:
            seq[k] = R[j]
            j = j + 1

# inputs: seq: Array of elements
#		  p: first position of the Array
#		  r: last position of the Array
# returns: Nothing. The function sorts the given array in place
def mergesort(seq,p,r):
    if p < r:
        q = (p + r) // 2
        mergesort(seq,p,q)
        mergesort(seq,q+1,r)
        merge(seq,p,q,r)

