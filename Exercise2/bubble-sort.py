#​​Write a function to sort an array using Bubble Sort  [5, 3, 8, 1, 2]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        if not swapped:
            break 
    return arr

arr = [5, 3, 8, 1, 2]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
