# s04-greedy

[55. Jump Game](https://leetcode.com/problems/jump-game/)

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index_, or `false` otherwise.

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 105`

## Notes

Backtracking starts at the root of a tree, and traverses through the first node and its children. If the node is good, then you are done. If the node is bad, then check each of its children until you have found a node that is good. If the all nodes are bad, you will need to "backtrack" to a previous node and traverse through each children, to find an option that is good. You try all the possible options (recursive), and then pick the most optimal route. 
Time: O(2^n) ???
Space: O(n!) ???

Greedy ???
From a given position, if we can find a good position, we only ever need one - the first one. If we keep track of this position, we can avoid searching for it, and also stop using the array altogether.
Time: O(n)
Space: O(1)

## Misc

* [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
