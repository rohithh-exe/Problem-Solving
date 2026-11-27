# LeetCode 1470 — Shuffle the Array

**Difficulty:** Easy  
**Topics:** Arrays, Indexing, `zip()`  
**Language:** Python  
**Status:** Solved

## Problem Statement

Given an array `nums` consisting of `2n` elements in the form:

`[x1, x2, ..., xn, y1, y2, ..., yn]`

Return the array in the following order:

`[x1, y1, x2, y2, ..., xn, yn]`

### Example 1

**Input:**
```python
nums = [2, 5, 1, 3, 4, 7]
n = 3
```

**Output:**
```python
[2, 3, 5, 4, 1, 7]
```

### Example 2

**Input:**
```python
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
```

**Output:**
```python
[1, 4, 2, 3, 3, 2, 4, 1]
```

## My Approach — Using `zip()` and Array Indexing

I solved this problem by using Python's `zip()` function to iterate through two ranges simultaneously.

The first range accesses the first half of the array, while the second range accesses the second half.

For each pair of indices, I append the corresponding elements to a new result list.

### Algorithm

1. Initialize an empty list `ans`.
2. Create two index ranges:
   - `range(len(nums))` for indices starting from zero.
   - `range(n, len(nums))` for indices in the second half.
3. Use `zip()` to iterate through both ranges simultaneously.
4. Append `nums[i]` to `ans`.
5. Append `nums[j]` to `ans`.
6. Repeat until `zip()` finishes.
7. Return the shuffled array.

## Python Solution

```python
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []

        for i, j in zip(range(len(nums)), range(n, len(nums))):
            ans.append(nums[i])
            ans.append(nums[j])

        return ans
```

## Step-by-Step Dry Run

**Input:** `nums = [2, 5, 1, 3, 4, 7]`, `n = 3`

| Iteration | i | j | nums[i] | nums[j] | ans |
|---|---|---|---|---|---|
| 1 | 0 | 3 | 2 | 3 | [2, 3] |
| 2 | 1 | 4 | 5 | 4 | [2, 3, 5, 4] |
| 3 | 2 | 5 | 1 | 7 | [2, 3, 5, 4, 1, 7] |

**Final Output:**
```python
[2, 3, 5, 4, 1, 7]
```

## Understanding `zip()`

The `zip()` function combines elements from two iterables into pairs.

Example:

```python
a = [0, 1, 2]
b = [3, 4, 5]

for i, j in zip(a, b):
    print(i, j)
```

**Output:**
```text
0 3
1 4
2 5
```

By default, `zip()` stops when the shortest iterable is exhausted.

In this problem, that gives exactly `n` pairs of indices.

## Mistake and Debugging Experience

During my initial implementation, I encountered an indexing error and researched how to iterate with two variables in one loop.

I discovered Python's `zip()` function and experimented with combining it with negative indexing.

My initial code included:

```python
j = i - n
```

This produced negative indices that accessed the correct elements from the second half of the array.

For example:

```python
nums[3]   # 3
nums[-3]  # 3
```

Both access the same element, but through different index representations.

I later understood that `zip()` already provides the required second-half index, so the reassignment was unnecessary.

Removing it made the implementation simpler and clearer.

## Complexity Analysis

### Time Complexity: O(n)

The `zip()` loop executes `n` times because the second range contains `n` indices.

Each iteration performs two array accesses and two append operations, each taking O(1) amortized time.

Therefore:

**Time Complexity = O(n)**

### Space Complexity: O(n)

The result list contains `2n` elements.

Since constant factors are ignored in Big-O notation:

**Space Complexity = O(n)**

The `zip()` object and range objects use O(1) additional space, excluding the output list.

## Submission Performance

| Metric | Result |
|---|---|
| Runtime | 56 ms |
| Runtime Beats | 96.54% |
| Memory | 19.12 MB |
| Memory Beats | 83.91% |

These measurements are from my LeetCode submission and may vary between runs.

## What I Learned

- How to use `zip()` to iterate over two ranges simultaneously.
- How to access elements from different halves of an array.
- How positive and negative indexing work in Python.
- How to debug index-related errors.
- How to simplify code by removing unnecessary operations.
- How to build a new array using `append()`.
- How to calculate time and space complexity.

## Conclusion

I solved LeetCode #1470 using Python's `zip()` function and array indexing.

This problem helped me learn a new Python feature through independent research and strengthened my understanding of array manipulation, debugging, and implementation logic.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)