# LeetCode 1365 — How Many Numbers Are Smaller Than the Current Number

**Difficulty:** Easy  
**Topics:** Arrays, Nested Loops, Comparison  
**Language:** Python  
**Status:** Submitted

## Problem Statement

Given an array of integers `nums`, return an array `result` where `result[i]` represents the number of elements in `nums` that are strictly smaller than `nums[i]`.

Elements with equal values are not counted.

### Example

**Input:**
```python
nums = [8, 1, 2, 2, 3]
```

**Output:**
```python
[4, 0, 1, 1, 3]
```

**Explanation:**

- `8` has 4 smaller elements.
- `1` has 0 smaller elements.
- Each `2` has 1 smaller element.
- `3` has 3 smaller elements.

## My Approach — Nested Loops (Brute Force)

I solved this problem using two nested loops to compare each element with every element in the array.

The outer loop selects the current element, and the inner loop counts how many elements are smaller than it.

### Algorithm

1. Initialize an empty list called `result`.
2. Traverse the array using an outer loop.
3. Initialize `count = 0` for the current element.
4. Use an inner loop to compare the current element with every element in the array.
5. If `nums[j] < nums[i]`, increment `count`.
6. After the inner loop finishes, append `count` to `result`.
7. Return the completed `result` list.

## Python Solution

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
```

## Dry Run

**Input:** `nums = [8, 1, 2, 2, 3]`

| Current Element | Smaller Elements | Count | Result |
|---|---|---|---|
| 8 | 1, 2, 2, 3 | 4 | [4] |
| 1 | None | 0 | [4, 0] |
| 2 | 1 | 1 | [4, 0, 1] |
| 2 | 1 | 1 | [4, 0, 1, 1] |
| 3 | 1, 2, 2 | 3 | [4, 0, 1, 1, 3] |

**Final Output:**
```python
[4, 0, 1, 1, 3]
```

## Complexity Analysis

### Time Complexity: O(n²)

The outer loop executes `n` times.

For each outer iteration, the inner loop also executes `n` times.

Therefore, the total number of comparisons is:

`n × n = n²`

**Time Complexity: O(n²)**

### Space Complexity: O(n)

The `result` list stores one integer for every element in the input array.

Therefore, the output requires O(n) space.

The algorithm uses O(1) auxiliary space when the output list is excluded.

## Submission Performance

| Metric | Result |
|---|---|
| Runtime | 159 ms |
| Runtime Beats | 15.76% |
| Memory | 19.04 MB |
| Memory Beats | 88.92% |

These values are from my submission and may vary between runs.

## What I Learned

- How to use nested loops to compare array elements.
- How to distinguish indices (`i`, `j`) from values (`nums[i]`, `nums[j]`).
- Why a counter must be reset for each new element.
- How to use strict comparison (`<`) to exclude equal values.
- How to construct an output array using `append()`.
- How to calculate O(n²) time complexity for nested loops.
- Why a correct brute-force solution may still have opportunities for optimization.

## Future Improvement

My current solution compares every element against every other element.

I plan to investigate ways to reduce repeated comparisons and improve the time complexity while developing the optimized approach independently.

## Conclusion

I implemented a nested-loop solution to count the number of smaller elements for each array element. This problem strengthened my understanding of indexing, nested loops, comparisons, and complexity analysis.