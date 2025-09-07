## Bubble Sort
Bubble sort compares repeatedly adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

The steps:
- Compare consecutive pairs of elements
- Swap elements in pair such that smaller is first
- when reaching end of list, start over again
- stop when no more swaps have been made
-> Time complexity = O(n^2)
## Insertion Sort
In-place, stable sorting algorithm. The "Left" part of the list is considered to be sorted, and elements in the "right" part of the list are inserted at the correct location in a sorted part of the list.

The steps:
- Start with the second element in the list
- Shift the current element to the left if it is smaller than the elements to the left
- Repeat until the last entry has been correctly inserted
-> Time complexity = O(n^2)
## Merge Sort
The merge sort algorithm follows the design principle of [[Basics of Algorithms#Divide & Conquer|Divide & Conquer]] and consists of two parts:
- Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted). Time complexity O(log(n))
- Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list. Time complexity O(n)
	- We merge by comparing elements from both halves and place the smaller element in the result array.
-> Time complexity = O(nlog(n))
