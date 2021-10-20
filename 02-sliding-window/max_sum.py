# Given an array of integers, find the maximum sum of a contiguous subarray of a specified length.

arr1 = [-1, 2, 3, 1, -3, 2]
i1 = 1
n1 = 2
s1 = 5
maxSum1 = 5
max1 = 3

# get the sum of a subarray
def getSumOfSubArray(arr, i, n):
    sum = 0
    for x in range(i, i + n):
        print(x)
        sum += arr[x]
        print(sum)
    return sum

# get the maximum value of array
def getMaxOfArray(arr):
    max = 0
    for x in range(len(arr)):
        if (max < arr[x]):
            max = arr[x]
    return max

# get the maximum sum of array
def getMaxSumOfArray(arr, n):
    maxSum = -999
    for x in range(len(arr) - n):
        currentSum = getSumOfSubArray(arr, x, n)
        if (maxSum < currentSum):
            maxSum = currentSum
    return maxSum

print(getSumOfSubArray(arr1, i1, n1))
print(getMaxOfArray(arr1) == max1)
print(getMaxSumOfArray(arr1, n1) == maxSum1)
