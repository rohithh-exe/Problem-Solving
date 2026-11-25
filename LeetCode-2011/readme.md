# LeetCode 2011 — Final Value of Variable After Performing Operations

**Difficulty:** Easy  
**Language:** Python  
**Topics:** Loops, Conditions, Simulation

**Problem:** https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

## Problem Description

Given a list of operations, find the final value of X, starting from X = 0.

- `++X` or `X++` increases X by 1.
- `--X` or `X--` decreases X by 1.

## My Approach

1. Initialize `x = 0`.
2. Traverse the operations using a for loop.
3. Check whether the operation increases X.
4. If yes, increment X. Otherwise, decrement X.
5. Return the final value of X.

## Python Solution

```python
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for operator in operations:
            if operator == "++X" or operator == "X++":
                x = x + 1
            else:
                x = x - 1
        return x
```

## Complexity Analysis

**Time Complexity:** O(n)

The loop processes each operation once.

**Auxiliary Space Complexity:** O(1)

Only a fixed amount of extra memory is used.

## What I Learned

- Using for loops to process a list.
- Using if-else conditions.
- Updating a variable.
- Understanding time and space complexity.
- Debugging case-sensitive string comparisons.
