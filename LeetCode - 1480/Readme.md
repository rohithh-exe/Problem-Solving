
# 1480. Running Sum of 1d Array

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topic:** Arrays, Prefix Sum

**Problem Link:** https://leetcode.com/problems/running-sum-of-1d-array/

## Problem Description

Given an array of integers, calculate the
running sum of the array.

## Example

Input: [1, 2, 3, 4]

Output: [1, 3, 6, 10]

## My Approach

1. Initialize total = 0.
2. Create an empty result list.
3. Traverse the array using a for loop.
4. Add each number to total.
5. Append the total to result.
6. Return the result list.

## Python Solution

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for num in nums:
            total += num
            result.append(total)

        return result
```

## Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

## What I Learned

- Array traversal
- Running sum
- List append operation
- Prefix sum basics
