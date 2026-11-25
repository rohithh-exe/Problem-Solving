# 412. Fizz Buzz

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topics:** Loops, Conditions, Modulo Operator

**Problem Link:** https://leetcode.com/problems/fizz-buzz/

## Problem Description

Given an integer `n`, return a list of strings representing numbers from 1 to n.

- If a number is divisible by both 3 and 5, return `"FizzBuzz"`.
- If divisible by 3, return `"Fizz"`.
- If divisible by 5, return `"Buzz"`.
- Otherwise, return the number as a string.

## Example

**Input:**
```python
n = 5
```

**Output:**
```python
["1", "2", "Fizz", "4", "Buzz"]
```

## My Approach

1. Create an empty list called `result`.
2. Use a `for` loop to iterate from 1 to n.
3. Check if the number is divisible by both 3 and 5.
4. Otherwise, check if it is divisible by 3 or 5.
5. Append the appropriate string to the result list.
6. Return the result list.

## Python Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
```

## Complexity Analysis

**Time Complexity:** O(n)

We iterate through numbers from 1 to n once.

**Space Complexity:** O(n)

We create a list containing n strings.

## What I Learned

- Using `for` loops with `range()`.
- Using `if`, `elif`, and `else`.
- Checking divisibility using `%`.
- Combining conditions using `and`.
- Converting integers to strings using `str()`.
- Understanding time and space complexity.
