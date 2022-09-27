
def maxSum(arr,WindowSize):
    arraySize = len(arr)
    if(arraySize<=WindowSize):
        print("Invalid Operation")
        return -1
    window_sum = sum([arr[i] for i in range(WindowSize)])
    max_sum = window_sum
    for i in range(arraySize-WindowSize):
        window_sum = window_sum - arr[i] + arr[i+WindowSize]
        max_sum = max(window_sum, max_sum)
    return max_sum

arr = [80,-50, 90, 100]
k = 2
answer = maxSum(arr,k)
print(answer)