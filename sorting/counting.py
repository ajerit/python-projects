# 
# Adolfo Jeritson
# Counting sort implementation. Sorting in linear time
# 2015
#

# inputs: A: Array of elements
#		  k: max number of elements
# returns: Nothing. The function sorts the given array in place
def countingsort(A,k):
    B = [0 for x in range(len(A))]
    C = [0 for x in range(k+1)]
        
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
          
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B