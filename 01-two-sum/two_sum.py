def two_sum(arr, target):
    arr.sort()
    l = 0
    r = len(arr) - 1

    while l < r:
        sum = arr[l] + arr[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [arr[l], arr[r]]
    return []

arr1 = [-1, 1, 2, 3, 5]
x1 = 5
a1 = [2,3]
print(two_sum(arr1, x1) == a1)

arr2 = [0, -1, 1]
x2 = 0
a2 = [-1, 1]
print(two_sum(arr2, x2) == a2)

arr3 = [-10, 2, 2, 8, 3]
x3 = 99
a3 = []
print(two_sum(arr3, x3) == a3)
