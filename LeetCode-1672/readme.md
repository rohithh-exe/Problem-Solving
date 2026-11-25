# 1672. Richest Customer Wealth

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topic:** Arrays, 2D Arrays

**Problem Link:** https://leetcode.com/problems/richest-customer-wealth/

## Problem Description

Given a 2D array `accounts`, find the maximum wealth among all customers. Each customer's wealth is the sum of the values in their list.

## Example

**Input:**
```python
accounts = [[1, 2, 3], [3, 2, 1], [4, 5, 1]]
```

**Output:**
```text
10
```

## My Approach

1. Initialize `max_wealth = 0`.
2. Use a `for` loop to visit each customer.
3. Calculate the customer's total wealth using `sum()`.
4. Compare the current wealth with `max_wealth`.
5. If the current wealth is greater, update `max_wealth`.
6. Return `max_wealth` after the loop.

## Python Solution

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            wealth = sum(customer)

            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth
```

## Complexity Analysis

**Time Complexity: O(m × n)**

Where `m` is the number of customers and `n` is the number of accounts per customer. We visit every account once.

**Space Complexity: O(1)**

We use only a fixed number of extra variables.

## What I Learned

- How to traverse a 2D array.
- How to calculate the sum of a list using `sum()`.
- How to find the maximum value using an `if` condition.
- How to calculate time and space complexity.
