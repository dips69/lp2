# .Implement Greedy search algorithm for any of the following application: I. Selection Sort

def selection_sort(arr):

    # Time complexity: O(n^2)
    # Space complexity: O(1)


    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Take user inputs for the array
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
#map converts each substring (which represents an element of the array entered by the user) into an integer.
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

# def selectionSort(array, size):
#     for val in range(size):
#         minvalue = val
#         for i in range(val+1, size):
#             if(arr[i]<arr[minvalue]):
#                 minvalue = i
#         (array[val],array[minvalue]) = (array[minvalue], array[val])

# arr = [6,3,5,2,1,4]
# length = len(arr)
# print("Original Array is:",arr)
# selectionSort(arr, length)
# print("After swapping", arr)
