from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # A good index is an index position that can reach the last index.

        # Set the initial last good index as the last index.
        last_good_index = len(nums) - 1

        # Traverse backwards, and track the last good index.
        for i in range(len(nums) - 2, -1, -1):

            # Compare whether the current index plus the index value (total jump) 
            # is greater or equal to the last good index.
            if (i + nums[i] >= last_good_index):
                last_good_index = i

        # If the last good index is not 0,
        # it cannot reach the last index.
        return last_good_index == 0

    def canJumpForward(self, nums: List[int]) -> bool:

        a = 0

        for i in range(len(nums)):
            if (i > a):
                return False
            a = max(i + nums[i], a)
        
        return True


# Testcase:

arr1 = [2,3,1,1,4]
a1 = True

arr2 = [3,2,1,0,4]
a2 = False

arr3 = [3, 0, 2, 0, 0, 1]
a3 = False

def test():
    print(Solution().canJump(arr1) == a1)
    print(Solution().canJump(arr2) == a2)
    print(Solution().canJump(arr3) == a3)
    print(Solution().canJumpForward(arr1) == a1)
    print(Solution().canJumpForward(arr2) == a2)
    print(Solution().canJumpForward(arr3) == a3)

def main():
    test()

if __name__ == "__main__":
    main()
