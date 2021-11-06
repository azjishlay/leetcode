from typing import List

class Solution:


    def get_mid_index(self, startIndex, endIndex):
        return (startIndex + endIndex) // 2

    def get_pivot_index(self, arr, startIndex, endIndex):
        # The pivot value is the starting value of the sorted array (i.e. before rotated).
        # The pivot value is the minimum value.
        # The purpose of finding the pivot index to use the rotated array as two sorted arrays.

        # If the array is not rotated (i.e. sorted), then the pivot is 0.
        if (arr[startIndex] <= arr[endIndex]):
            return 0

        while (startIndex <= endIndex):

            mid = self.get_mid_index(startIndex, endIndex)

            # print(startIndex, mid, endIndex)

            if (arr[mid] > arr[mid + 1]):
                return mid + 1
            elif (arr[startIndex] < arr[mid]):
                startIndex = mid + 1
            else:
                endIndex = mid - 1

    def search(self, nums: List[int], target: int) -> int:

        print(nums, " : ", target)

        n = len(nums)
        
        startIndex = 0
        endIndex = n - 1

        pivotIndex = self.get_pivot_index(nums, startIndex, endIndex)

        print("pivot:", pivotIndex)

        # Binary search only works on sorted arrays.
        # Binary search compares an element in the middle of the array to the target value, and based on the value comparison, repeats the search to the left or right.

        while (startIndex <= endIndex):

            mid = self.get_mid_index(startIndex, endIndex)

            # ???
            r = (mid + pivotIndex) % n

            print(startIndex, mid, endIndex)

            # Compare the mid value to target.
            if (nums[r] == target):
                return r
            # If the mid value is less than the target, 
            # search to the right.
            elif (nums[r] < target):
                startIndex = mid + 1
            else:
                # Else, search to the left.
                endIndex = mid - 1

        # Target not found!
        return -1

# Testcase:

arr0 = [0, 1, 2, 4, 5, 6, 7]
piv0 = 0
x0 = 0
a0 = 0

arr1 = [4, 5, 6, 7, 0, 1, 2]
piv1 = 4
x1 = 0
a1 = 4

arr2 = [5, 6, 7, 0, 1, 2, 4]
piv2 = 3
x2 = 8
a2 = -1

arr3 = [6, 7, 0, 1, 2, 4, 5]
piv3 = 2
x3 = 6
a3 = 0

arr4 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2]
piv4 = 13
x4 = 23
a4 = -1

def test_get_pivot_index():
    print(Solution().get_pivot_index(arr0) == piv0)
    print(Solution().get_pivot_index(arr1) == piv1)
    print(Solution().get_pivot_index(arr2) == piv2)
    print(Solution().get_pivot_index(arr3) == piv3)
    print(Solution().get_pivot_index(arr4) == piv4)

def test():
    # print(Solution().search(arr0, x0) == a0)
    # print(Solution().search(arr1, x1) == a1)
    print(Solution().search(arr2, x2) == a2)
    print(Solution().search(arr3, x3) == a3)
    print(Solution().search(arr4, x4) == a4)

def main():
    # test_get_pivot_index()
    test()

if __name__ == "__main__":
    main()
