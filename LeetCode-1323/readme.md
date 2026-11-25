# 1323. Maximum 69 Number

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topics:** Greedy, String Manipulation, Loops

**Problem Link:** https://leetcode.com/problems/maximum-69-number/

## Problem Description

Given a positive integer containing only the digits `6` and `9`, return the maximum possible number by changing at most one digit.

- Change `6` to `9`.
- Or change `9` to `6`.
- You can change at most one digit.

## Example

**Input:**
```python
num = 9669
```

**Output:**
```text
9969
```

**Explanation:**

Changing the first `6` to `9` gives the maximum possible number.

## My Approach

1. Convert the given integer into a list of digit characters.
2. Iterate through the digits from left to right.
3. Check whether the current digit is `"6"`.
4. Change the first `"6"` to `"9"`.
5. Use `break` to stop the loop after one change.
6. Combine the digits into a string using `join()`.
7. Convert the string back to an integer and return it.

## Python Solution

```python
class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))

        for i in range(0, len(digits)):
            if digits[i] == "6":
                digits[i] = "9"
                break

        result = "".join(digits)
        return int(result)
```

## Complexity Analysis

**Time Complexity: O(d)**

Here, `d` is the number of digits in the input. Converting the number to a string, searching for the first `6`, and joining the digits each take at most O(d) time.

**Space Complexity: O(d)**

We create a list of digits and a new string, both requiring space proportional to the number of digits.

## What I Learned

- Converting integers into strings and lists.
- Accessing and modifying list elements using indices.
- Using `for` loops and `if` conditions.
- Using `break` to stop a loop.
- Combining characters using `join()`.
- Converting strings back to integers.
- Using a greedy approach to find the maximum number.
