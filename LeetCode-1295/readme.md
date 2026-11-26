# LeetCode 1295 — Find Numbers with Even Number of Digits

**Difficulty:** Easy  
**Topic:** Arrays, Strings, Iteration  
**Language:** Python

## Problem Statement

Given an array of integers `nums`, return how many numbers contain an even number of digits.

### Example 1

**Input:**
```python
nums = [12, 345, 2, 6, 7896]
```

**Output:**
```python
2
```

**Explanation:**

- `12` has 2 digits — even.
- `345` has 3 digits — odd.
- `2` has 1 digit — odd.
- `6` has 1 digit — odd.
- `7896` has 4 digits — even.

Therefore, the answer is `2`.

## My Approach — String Conversion

I solved this problem by converting each number into a string and checking its length.

### Algorithm

1. Initialize a counter to zero.
2. Traverse each number in the input array.
3. Convert the current number to a string using `str()`.
4. Find the number of digits using `len()`.
5. If the digit count is divisible by 2, increment the counter.
6. Return the final counter.

## Python Solution

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1

        return count
```

## Dry Run

**Input:** `nums = [12, 345, 2, 6, 7896]`

| Number | String | Digit count | Even? | Count |
|---|---|---|---|---|
| 12 | "12" | 2 | Yes | 1 |
| 345 | "345" | 3 | No | 1 |
| 2 | "2" | 1 | No | 1 |
| 6 | "6" | 1 | No | 1 |
| 7896 | "7896" | 4 | Yes | 2 |

**Final output:** `2`

## Complexity Analysis

**Time Complexity: O(n × d)**

Where:
- `n` = number of elements in the array.
- `d` = maximum number of digits in an element.

Each number is converted into a string, which takes time proportional to its digit count.

**Auxiliary Space Complexity: O(d)**

String conversion temporarily creates a string containing the digits of the current number.

For LeetCode #1295, the maximum digit count is bounded, so both complexities can also be expressed as O(n) time and O(1) auxiliary space.

## Mistake I Made

Initially, I tried converting the entire list into a string:

```python
nums = str(nums)
```

This was incorrect because the problem requires checking the digit count of each individual number, not the complete list.

I corrected this by converting each element separately inside the loop:

```python
len(str(i))
```

## What I Learned

- How to traverse a list element by element.
- How to use `str()` and `len()` together.
- How to check even numbers using `% 2`.
- The difference between processing an entire list and processing its individual elements.
- How to analyze the time and auxiliary space complexity of a solution.

## Result

**Status:** Accepted

Successfully solved LeetCode #1295 using Python.