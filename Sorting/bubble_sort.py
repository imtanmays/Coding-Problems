'''
Topic  : Sorting
Problem: Bubble Sort
Runtime: O(n^2)
Space  : O(1)

''' 
from check import expect

def bubble_sort(array,array_len):
	for j in range(0,array_len-1): 
		for i in range(0,array_len-1-j):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
	return array


# Tests
a1 = [9,8,7,6,5]
a2 = [3,0,8,2,4,9,1]
a3 = [1,2,3]
a4 = []
a5 = [7]

print(expect([5,6,7,8,9],bubble_sort(a1,5)))
print(expect([0,1,2,3,4,8,9],bubble_sort(a2,7)))
print(expect([1,2,3],bubble_sort(a3,3)))
print(expect([],bubble_sort(a4,0)))
print(expect([7],bubble_sort(a5,1)))