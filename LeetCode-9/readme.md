# 9. Palindrome Number

**Platform:** LeetCode  
**Difficulty:** Easy  
**Language:** Python  
**Topics:** Math, While Loop, Modulo Operator, String Manipulation

**Problem Link:** https://leetcode.com/problems/palindrome-number/

## Problem Description

Given an integer `x`, return `True` if it is a palindrome and `False` otherwise.

A palindrome number reads the same forward and backward.

**Follow-up:** Can you solve the problem without converting the integer into a string?

## Example

**Input:**
```python
x = 121
```

**Output:**
```text
True
```

**Explanation:** Reversing `121` gives `121`, so it is a palindrome.

## Approach 1: Mathematical Method (My Approach)

I solved this problem without converting the integer into a string.

### Logic

1. Store the original number in a separate variable.
2. Initialize `reversed_num = 0`.
3. Use a `while` loop to process the digits.
4. Extract the last digit using `% 10`.
5. Build the reversed number by multiplying the existing reversed number by 10 and adding the extracted digit.
6. Remove the last digit using `// 10`.
7. Compare the reversed number with the original number.
8. Return `True` if both are equal; otherwise, return `False`.

### Python Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        return reversed_num == original
```

### Dry Run

For `x = 121`:

| Step | Extracted Digit | Reversed Number | Remaining x |
|---|---|---|---|
| Initial | — | 0 | 121 |
| 1 | 1 | 1 | 12 |
| 2 | 2 | 12 | 1 |
| 3 | 1 | 121 | 0 |

Since `reversed_num == original`, the result is `True`.

### Complexity Analysis

**Time Complexity: O(log n)**

The loop processes each digit once.

**Space Complexity: O(1)**

Only a fixed number of variables are used.

---

## Approach 2: String Conversion Method (Alternative)

This approach converts the number into a string and compares it with its reversed version.

### Logic

1. Convert the integer into a string using `str()`.
2. Reverse the string using `[::-1]`.
3. Compare the original string with the reversed string.
4. Return the comparison result.

### Python Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        return text == text[::-1]
```

### Complexity Analysis

**Time Complexity: O(log n)**

Converting and reversing the digits takes time proportional to the number of digits.

**Space Complexity: O(log n)**

The string and its reversed copy require additional memory.

---

## Comparison of Both Approaches

| Feature | Mathematical Method | String Method |
|---|---|---|
| Uses string conversion | No | Yes |
| Uses modulo `%` | Yes | No |
| Uses `while` loop | Yes | No |
| Time Complexity | O(log n) | O(log n) |
| Space Complexity | O(1) | O(log n) |
| Satisfies follow-up | Yes | No |
| Implementation | More steps | Shorter |

## What I Learned

- Extracting the last digit using `% 10`.
- Removing the last digit using `// 10`.
- Reversing a number mathematically.
- Using a `while` loop.
- Comparing numbers using `==`.
- Understanding the difference between `return` and `print`.
- Comparing mathematical and string-based solutions.
- Understanding time and space complexity.

## Conclusion

I solved this problem using the **mathematical approach without string conversion**, satisfying the follow-up challenge.

I also learned the alternative string conversion approach, which is shorter and easier to implement.

Both approaches have the same asymptotic time complexity, but the mathematical approach uses constant extra space.
