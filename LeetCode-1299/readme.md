# 1299. Replace Elements with Greatest Element on Right Side

**Difficulty:** Easy  
**Topic:** Arrays  
**Language:** Python  
**LeetCode:** https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

## Problem Description

Given an array `arr`, replace every element with the greatest element among the elements to its right. Replace the last element with `-1`.

### Example

**Input:**
```python
arr = [17, 18, 5, 4, 6, 1]
```

**Output:**
```python
[18, 6, 6, 6, 1, -1]
```

## Approach 1: Brute Force

### My Initial Approach

My first idea was to check all the elements to the right of each position and find the maximum.

1. Create an empty result list.
2. For every element except the last, initialize the maximum using the next element.
3. Use an inner loop to examine the remaining elements on the right.
4. Append the greatest value found to the result.
5. Append `-1` for the last element.

### Code

```python
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = []
        for i in range(len(arr)-1):
            maximum = arr[i + 1]
            for j in range(i+1, len(arr)-1):
                current = arr[j + 1]
                if current > maximum:
                    maximum = current
            result.append(maximum)
        result.append(-1)
        return result
```

### Complexity

- **Time:** O(n²), because of the nested loops.
- **Space:** O(n), because a separate result list is created.

### Submission Result

The initial solution exceeded the time limit (TLE), passing 38 out of 90 test cases.

## Approach 2: Optimized Right-to-Left Traversal

### What I Learned

Instead of repeatedly searching the elements to the right, I can traverse the array from right to left while maintaining a running maximum.

At each position:

1. Save the original element before overwriting it.
2. Replace the current element with the maximum found so far on its right.
3. Update the running maximum using the saved original element.

The order matters because overwriting an element too early would lose information needed for the remaining positions.

### My Optimized Code

```python
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1

        for i in range(len(arr)-1, -1, -1):
            original = arr[i]
            arr[i] = maximum
            maximum = max(maximum, original)

        return arr
```

### Dry Run

**Input:** `[17, 18, 5, 4, 6, 1]`

| Original element | Maximum to its right | Replacement | Updated maximum |
|---|---|---|---|
| 1 | -1 | -1 | 1 |
| 6 | 1 | 1 | 6 |
| 4 | 6 | 6 | 6 |
| 5 | 6 | 6 | 6 |
| 18 | 6 | 6 | 18 |
| 17 | 18 | 18 | 18 |

**Final output:** `[18, 6, 6, 6, 1, -1]`

### Complexity

- **Time:** O(n), because every element is processed once.
- **Extra space:** O(1), because the algorithm uses only a constant number of variables and modifies the input array in place.

## What I Learned from This Problem

- How to recognize repeated work in nested loops.
- How to optimize a brute-force approach using a running maximum.
- How to traverse an array from right to left.
- Why preserving an original value is important during in-place modification.
- How to avoid off-by-one errors in Python's `range()`.
- The difference between understanding an algorithm and independently implementing it.

## Key Takeaway

My initial brute-force approach was logically correct but too slow for large inputs. By using a single reverse traversal and remembering the maximum value, I reduced the time complexity from **O(n²) to O(n)** and the extra space complexity from **O(n) to O(1)**.
