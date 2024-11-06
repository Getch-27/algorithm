
def max_heapify(A, i):
    """
    performs max heapify operation on a given array A at index i.
    It ensures that the subtree rooted at index i is a max heap.

    Parameters:
    A (list): The input array to be transformed into a max heap.
    i (int): The index of the node to be heapified.

    Returns:
    None. The function modifies the input array A in-place.
    """
    n = len(A)  
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right

    # If the largest is not the current index, swap and recurse
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def heapify(A):
    """
    This function transforms the input array A into a max heap.
    It starts from the last non-leaf node and heapifies each subtree rooted at that node.
    
    Parameters:
    A (list): The input array to be transformed into a max heap. The array must be a complete binary tree.
    
    Returns:
    None. The function modifies the input array A in-place.
    """
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i)

def heap_sort(A):
    """
    Sorts the input list `A` in ascending order using the heap sort algorithm.
    
    The algorithm builds a max heap from the input list and then repeatedly swaps
    the root (largest element) with the last element of the heap. After each swap,
    the heap is reduced in size and the heap property is restored by calling `max_heapify`
    on the root of the reduced heap. This process continues until all elements are sorted.
    
    Parameters:
        A (list): A list of elements that will be sorted in place.
    
    
    Time Complexity:
        - Building the max heap takes O(n).
        - Extracting elements and restoring the heap takes O(n log n).
        Therefore, the overall time complexity is O(n log n).
    
    Space Complexity:
        - The algorithm sorts in place, so the space complexity is O(1).
    """
    heapify(A)  # Step 1: Build max-heap

    # Step 2: Extract elements one by one from heap
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  
        subarray = A[:i]  
        max_heapify(subarray, 0)  
        A[:i] = subarray 

A = [3, 5, 1, 10, 2, 7 , 9 , 1 , 12]
heap_sort(A)
print("Sorted array:", A)
