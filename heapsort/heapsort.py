'''
If i is the index of the current node, then
iParent     = floor((i-1) / 2)
iLeftChild  = 2*i + 1
iRightChild = 2*i + 2
'''
from math import floor

def sift_down(array, start, end):
	'''
	This function maintains the heap order
	'''
	root = start

	while root * 2 + 1 <= end: # while root has at least 1 child
		# sift down the node at index start to the proper place
		# such that all nodes below the start index are in heap
		# order
		child = root * 2 + 1 # left child
		swap = root # keep track of child to swap with

		if array[swap] < array[child]:
			swap = child
		# if there is a right child and that child is greater
		if child + 1 <= end and array[swap] < array[child+1]:
			swap = child + 1
		if swap != root:
			temp = array[root]
			array[root] = array[swap]
			array[swap] = temp
			root = swap
			# repeat to continue sifting down the child now
		else:
			# if the root is larger than its children,
			# we don't need to sift down anymore
			break


def heapfiy(array):
	# start is assinged the index in array of the 
	# last parent node
	# the last element in a 0-based array is at len(array)-1;
	# find the parent of that element
	start = (len(array)-2)/2

	while start >= 0:
		# sift down the node at index start to the proper place
		# such that all nodes below the start index are in 
		# heap order
		sift_down(array, start, len(array)-1)
		# go to the next parent node
		start = start - 1


def heapsort(array):

	# build the heap in array so that largest value is at the root
	print "Heapfiy the array: "
	heapfiy(array)
	print array

	print "Sorting the array using heapsort: "
	# the following loop maintains the invariants that array[0:end]
	# is a heap and every element beyond end is greater than
	# everything 
	end = len(array) - 1
	while end > 0:
		# array[0] is the root and the largest value
		# the swap moves it in front of the sorted elements
		temp = array[end]
		array[end] = array[0]
		array[0] = temp
		# the heap size is reduced by 1
		end = end - 1
		print array
		sift_down(array, 0, end)
	print array


if __name__ == "__main__":
	# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
	# heapsort(l1)
	# print l1

	# l2 = [9, 8, 7, 6, 5, 4, 3, 2]
	# heapsort(l2)
	# print l2

	import random
	l3 = [random.randint(-100, 100) for i in range(10)]
	print "Initial array: "
	print l3
	print "Start heapsort: "
	heapsort(l3)
	print l3
