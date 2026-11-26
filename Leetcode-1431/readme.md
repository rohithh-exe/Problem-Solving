# 1431. Kids With the Greatest Number of Candies

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topics:** Array, Loop, Conditional Statements

**Problem Link:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

## Problem Description

Given an integer array `candies`, where `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`, return a Boolean array indicating whether each kid could have the greatest number of candies after receiving all the extra candies.

Multiple kids can have the greatest number of candies.

## Example

**Input:**
```python
candies = [2, 3, 5, 1, 3]
extraCandies = 3
```

**Output:**
```python
[True, True, True, False, True]
```

## My Approach — Maximum Value + For Loop + If-Else

I solved this problem using a simple `for` loop and conditional statements.

### Step-by-Step Logic

1. Find the maximum number of candies using `max(candies)`.
2. Create an empty list named `result`.
3. Iterate through each kid's candy count using a `for` loop.
4. Add `extraCandies` to the current kid's candy count for comparison.
5. If the total is greater than or equal to the original maximum, append `True`.
6. Otherwise, append `False`.
7. Return the result list after completing the loop.

## Python Solution

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []

        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)

        return result
```

## Dry Run

**Input:** `candies = [2, 3, 5, 1, 3]`, `extraCandies = 3`

**Maximum candies = 5**

| Kid | Original Candies | After Extra Candies | Comparison | Result |
|---|---|---|---|---|
| 1 | 2 | 5 | 5 >= 5 | True |
| 2 | 3 | 6 | 6 >= 5 | True |
| 3 | 5 | 8 | 8 >= 5 | True |
| 4 | 1 | 4 | 4 >= 5 | False |
| 5 | 3 | 6 | 6 >= 5 | True |

**Final Output:**
```python
[True, True, True, False, True]
```

## Complexity Analysis

**Time Complexity: O(n)**

- `max(candies)` takes O(n) time.
- The `for` loop visits every element once, taking O(n) time.
- Total: O(n) + O(n) = **O(n)**.

**Space Complexity: O(n)**

- The `result` list stores one Boolean value for each kid.
- Therefore, the output list requires O(n) space.
- Auxiliary space excluding the output list is O(1).

## What I Learned

- Finding the largest element using `max()`.
- Iterating through a list using a `for` loop.
- Comparing values using `>=`.
- Using `if-else` conditions.
- Appending Boolean values using `append(True)` and `append(False)`.
- Understanding the difference between strings `"True"` and Boolean values `True`.
- Placing `return` outside the loop to process every element.
- Understanding O(n) time complexity and output space.

## Conclusion

I successfully solved this problem using my own approach with `max()`, a `for` loop, and `if-else` conditions.

This problem helped me practice array traversal, conditional comparisons, Boolean values, and building a result list.
