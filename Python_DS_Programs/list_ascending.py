# Initialize array

try:
    arr = [5, 2, 8, 7, 1]
    temp = 0
    arr_temp = []

    # Displaying elements of original array
    print("Elements of original array: ")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")

    # Sort the array in ascending order
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        arr_temp.append(arr[i])
    print()
    print("Elements of array in list format: ")
    print(arr_temp)

    # Displaying elements of the array after sorting

    print("Elements of array sorted in ascending order without list format: ")
    for i in arr_temp:
        print(i, end=" ")

except:
    print("An exception occurred")
