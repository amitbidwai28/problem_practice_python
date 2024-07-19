# Initialize array

try:

    input_no = int(input("Enter the number"))
    arr=[]
    for ele in range(0,input_no):
        x=int(input())
        arr.append(x)
    print(arr)
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

    print("\nSmallest number in the list is :", arr_temp[0])
    highest_element = arr_temp[len(arr_temp)-1]
    print("Greatest number in the list is: ", highest_element)

except:
    print("An exception occurred")
