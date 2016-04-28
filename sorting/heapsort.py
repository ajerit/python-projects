#
# Adolfo Jeritson
# Heap sort implementation
# 2015
#

# Heap operations
def parent(i):
    return i//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

# Given a heap A, changes items places to the max heap property
def max_heapify(A, i, size):
    l = left(i)
    r = right(i)
    if l <= size and A[l] > A[i]:
        largest = l
    else:
		largest = i
    if r <= size and A[r] > A[largest]:
            largest = r
    if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest, size)

def build_max_heap(A, size):
    for i in range((len(A)//2)-1,-1,-1):
        max_heapify(A, i, size)

# inputs: A: Array of elements
# returns: Nothing. The function sorts the given array in place
def heapsort(A):
    size = len(A)-1
    build_max_heap(A, size)
    for i in range(len(A)-1,-1,-1):
        A[0], A[i] = A[i], A[0]
        size = size - 1
        max_heapify(A, 0, size)
