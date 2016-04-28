#
# Adolfo Jeritson
# Binary search implementation
# 2015
#

# inputs: A: Array of elements
#         x: Target element
# returns  None if the element is not found
#          the position in the array if the element is found
def binarySearch(A, x):
	start = 0
	end = len(A)
	while start < end:
		mid = (end+(start-end)) / 2
		if A[mid] == x:
			return mid
		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	return start if A[start] == x else None
