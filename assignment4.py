def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # sorting by using simultaneous assignment in python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr1input = input("Input array to sort: ")
arr2input = input("Input array to sort: ")
arr1 = list(arr1input)
arr2 = list(arr2input)
print('Before sorting an Integer Array: {}'.format(arr1))
bubble_sort(arr1)
print('After sorting an Integer Array: {}'.format(arr1))
print('Before sorting an String Array: {}'.format(arr2))
bubble_sort(arr2)
print('After sorting an String Array: {}'.format(arr2))