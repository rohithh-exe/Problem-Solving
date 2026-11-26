# 1512. Number of Good Pairs

**Platform:** LeetCode
**Difficulty:** Easy
**Language:** Python
**Topics:** Arrays, Nested Loops, Conditional Statements

**Problem Link:** [https://leetcode.com/problems/number-of-good-pairs/](https://leetcode.com/problems/number-of-good-pairs/)

## Problem Description

Given an array of integers `nums`, return the number of good pairs.

A pair `(i, j)` is considered good when both conditions are satisfied:

1. `nums[i] == nums[j]`
2. `i < j`

## Example

**Input:**

```python
nums = [1, 2, 3, 1, 1, 3]
```

**Output:**

```text
4
```

**Explanation:**

The good pairs are:

- `(0, 3)` — both values are 1
- `(0, 4)` — both values are 1
- `(3, 4)` — both values are 1
- `(2, 5)` — both values are 3

Total good pairs = 4.

## My Approach — Brute Force Using Nested Loops

I solved this problem using two `for` loops and an `if` condition to check whether each pair satisfies the requirements.

### Step-by-Step Logic

1. Initialize a counter variable `count = 0`.
2. Use the first `for` loop to iterate through the indices of the array using `i`.
3. Use the second `for` loop to iterate through the indices using `j`.
4. Check whether `nums[i] == nums[j]` and `i < j`.
5. If both conditions are satisfied, increment `count` by 1.
6. Continue checking the remaining index combinations.
7. Return the final count.

## My Python Solution

```python
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1

        return count
```

## Dry Run

**Input:** `nums = [1, 2, 1]`

| i | j | nums[i] | nums[j] | i < j | Good Pair? |
| - | - | ------- | ------- | ----- | ---------- |
| 0 | 0 | 1       | 1       | False | No         |
| 0 | 1 | 1       | 2       | True  | No         |
| 0 | 2 | 1       | 1       | True  | Yes        |
| 1 | 0 | 2       | 1       | False | No         |
| 1 | 1 | 2       | 2       | False | No         |
| 1 | 2 | 2       | 1       | True  | No         |
| 2 | 0 | 1       | 1       | False | No         |
| 2 | 1 | 1       | 2       | False | No         |
| 2 | 2 | 1       | 1       | False | No         |

**Final Output:**

```text
1
```

## Complexity Analysis

**Time Complexity: O(n²)**

- The outer loop runs `n` times.
- The inner loop runs `n` times for every outer iteration.
- Total iterations = `n × n = n²`.

Therefore, the time complexity is **O(n²)**.

**Auxiliary Space Complexity: O(1)**

- Only the counter and loop variables are used.
- No additional arrays or data structures are created.

Therefore, the auxiliary space complexity is **O(1)**.

## What I Learned

- Using nested `for` loops to compare array elements.
- Understanding the difference between array values and indices.
- Using `range(len(nums))` to access indices.
- Checking multiple conditions using `and`.
- Using `count += 1` to count valid pairs.
- Understanding brute-force algorithms.
- Calculating time complexity for nested loops.
- Identifying opportunities to optimize unnecessary comparisons.

## Conclusion

I successfully solved LeetCode #1512 using my own brute-force approach with nested loops and conditional statements.

The solution has O(n²) time complexity and O(1) auxiliary space complexity.

My next goal is to optimize the algorithm independently while maintaining correctness.
