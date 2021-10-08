# Given an array of integers, find the maximum sum of a contiguous subarray(s) of the specified length.

# Sliding window (static size):
# Calculate the sum of the elements inside the window.
# Slide the window over by one element at a time.

def max_sum_static(arr, window):
    a = 0

    if arr and len(arr) >= window:

        # gets the subarrays based on the specified length
        arrs = []
        for i in range(len(arr) - 1):
            arrs.append(arr[i:i + window])
        # print(arrs)

        # gets the sum of each subarray
        sums = []
        for i in range(len(arrs)):
            for j in range(len(arrs[i])):
                a += arrs[i][j]
            sums.append(a)
            a = 0
        # print(sums)

        # gets the largest sum
        a = 0
        for i in range(len(sums) - 1):
            if sums[i] > a:
                a = sums[i]

    return a

arr1 = [-1, 2, 3, 1, -3, 2]
n1 = 2
# [[-1, 2], [2, 3], [3, 1], [1, -3], [-3, 2]]
# [1, 5, 4, -2, -1]
a1 = 5
print(max_sum_static(arr1, n1) == a1)
