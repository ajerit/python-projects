#
# Adolfo Jeritson
# Linear searching implementation
# 2015
#

# inputs: A: Array of elements
#         x: Target element
# returns  None if the element is not found
#          the position in the array if the element is found
def linearSearch(A, x):
	for i in range(0, len(A)):
		if A[i] == x:
			return i
		return None