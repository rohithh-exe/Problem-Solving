# 1342. Number of Steps to Reduce a Number to Zero

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topics:** While Loop, Conditions, Math

**Problem Link:** https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

## Problem Description

Given a non-negative integer `num`, find the number of steps required to reduce it to zero.

- If the number is even, divide it by 2.
- If the number is odd, subtract 1.
- Repeat until the number becomes zero.

## Example

**Input:**
```python
num = 14
```

**Output:**
```text
6
```

**Explanation:**

14 → 7 → 6 → 3 → 2 → 1 → 0

Total steps = 6.

## My Approach

1. Initialize `count = 0` to track the number of steps.
2. Use a `while` loop until `num` becomes zero.
3. Check whether the number is even using `% 2`.
4. If even, divide the number by 2 using `//`.
5. Otherwise, subtract 1.
6. Increase the step count after each operation.
7. Return the total number of steps.

## Python Solution

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num != 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
            else:
                num = num - 1
                count += 1

        return count
```

## Complexity Analysis

**Time Complexity: O(log n)**

For positive `n`, the number decreases through repeated division by 2, with at most one subtraction between divisions.

**Space Complexity: O(1)**

Only a fixed number of variables are used.

## What I Learned

- Using a `while` loop.
- Checking even and odd numbers using `%`.
- Using integer division `//`.
- Updating variables inside a loop.
- Counting the number of iterations.
- Understanding logarithmic time complexity.
