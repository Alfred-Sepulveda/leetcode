def print2ndLargest(arr, arr_size):
    if (arr_size < 2):
        print("Invalid Input ")
        return
    arr.sort

    for i in range(arr_size-2,-1,-1):
        if (arr[i] != arr[arr_size -1]):
            print("The second Largest element is", arr[i])
            return
    print("there is no second largest element")


#Driver Code
arr = [25,-2,0,7,25,24,20]
n = len(arr)
print2ndLargest(arr,n)


#