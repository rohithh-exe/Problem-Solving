# LeetCode 1920 — Build Array from Permutation

**Difficulty:** Easy  
**Topics:** Arrays, Indexing, Simulation  
**Language:** Python  
**Status:** Solved

## Problem Statement

Given a zero-based permutation array `nums` containing `n` distinct integers from `0` to `n - 1`, build a new array `ans` such that:

`ans[i] = nums[nums[i]]`

Return the resulting array.

### Example 1

**Input:**
```python
nums = [0, 2, 1, 5, 3, 4]
```

**Output:**
```python
[0, 1, 2, 4, 5, 3]
```

### Example 2

**Input:**
```python
nums = [5, 0, 1, 2, 3, 4]
```

**Output:**
```python
[4, 5, 0, 1, 2, 3]
```

## My Approach — Array Traversal and Nested Indexing

I solved this problem using a `for` loop and an empty result list.

For each index `i`, I first access `nums[i]`. Then I use that value as another index to access `nums[nums[i]]`.

I append the resulting value to `ans`.

### Algorithm

1. Initialize an empty list `ans`.
2. Traverse every index of `nums` using `range(len(nums))`.
3. Access the value at the current index using `nums[i]`.
4. Use that value as another index to obtain `nums[nums[i]]`.
5. Append the obtained value to `ans`.
6. After the loop finishes, return `ans`.

## Python Solution

```python
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
```

## Step-by-Step Dry Run

**Input:** `nums = [0, 2, 1, 5, 3, 4]`

| i | nums[i] | nums[nums[i]] | ans |
|---|---|---|---|
| 0 | 0 | nums[0] = 0 | [0] |
| 1 | 2 | nums[2] = 1 | [0, 1] |
| 2 | 1 | nums[1] = 2 | [0, 1, 2] |
| 3 | 5 | nums[5] = 4 | [0, 1, 2, 4] |
| 4 | 3 | nums[3] = 5 | [0, 1, 2, 4, 5] |
| 5 | 4 | nums[4] = 3 | [0, 1, 2, 4, 5, 3] |

**Final Output:**

```python
[0, 1, 2, 4, 5, 3]
```

## Complexity Analysis

### Time Complexity: O(n)

The `for` loop traverses the input array exactly once.

Each nested indexing operation, `nums[nums[i]]`, takes O(1) time.

Therefore:

**Time Complexity = O(n)**

### Space Complexity: O(n)

A new list `ans` is created to store `n` elements.

Therefore:

**Space Complexity = O(n)**

The additional working space, excluding the output array, is O(1).

## Alternative Python Syntax — List Comprehension

After solving the problem, I observed that the same logic can be written using list comprehension:

```python
return [nums[nums[i]] for i in range(len(nums))]
```

Both approaches have:

- Time Complexity: O(n)
- Space Complexity: O(n)

List comprehension may have lower execution overhead in Python, but it does not change the underlying algorithm or its asymptotic complexity.

My original solution uses a regular `for` loop because it clearly shows each step of the process.

## Submission Performance

**Runtime:** 1 ms

The solution was submitted successfully on LeetCode.

Runtime results can vary between submissions and do not necessarily indicate a difference in algorithmic complexity.

## What I Learned

- How to access elements using array indices.
- How nested indexing works in Python.
- How to use `nums[nums[i]]` correctly.
- How to construct a new array using `append()`.
- How to traverse an array using `range(len(nums))`.
- How to calculate time and space complexity.
- How a regular `for` loop and list comprehension can implement the same algorithm.

## Conclusion

I independently solved LeetCode #1920 using array traversal and nested indexing.

This problem improved my confidence in converting problem statements into working Python code without implementation hints.

My solution has O(n) time complexity and O(n) space complexity.