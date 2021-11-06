def linear_search(nums, target):
    for i in range(len(nums)):
        # print(i)
        if (nums[i] == target):
            return i
    return -1

def pivot_linear_search(nums):
    for x in range(len(nums) - 1):
        # print(x)
        if (nums[x] > nums[x + 1]):
            return x + 1
    return 0


arr1 = [4, 5, 6, 7, 0, 1, 2]
piv1 = 4
x1 = 0
a1 = 4

print(linear_search(arr1, x1) == a1)
print(pivot_linear_search(arr1) == piv1)

arr2 = [5, 6, 7, 0, 1, 2, 4]
piv2 = 3
x2 = 8
a2 = -1

print(linear_search(arr2, x2) == a2)
print(pivot_linear_search(arr2) == piv2)

arr3 = [6, 7, 0, 1, 2, 4, 5]
piv3 = 2
x3 = 6
a3 = 0

print(linear_search(arr3, x3) == a3)
print(pivot_linear_search(arr3) == piv3)
