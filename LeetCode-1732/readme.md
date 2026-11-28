# 1732. Find the Highest Altitude

**Difficulty:** Easy  
**Topic:** Array, Prefix Sum  
**Language:** Python  
**Status:** Accepted

**Problem Link:** https://leetcode.com/problems/find-the-highest-altitude/

---

## Problem Description

A biker travels through several points at different altitudes.

The biker starts at altitude `0`. We are given an array `gain`, where each element represents the change in altitude between two consecutive points.

Our task is to find the **highest altitude reached during the journey**, including the starting altitude.

### Example 1

**Input:**
```python
gain = [-5, 1, 5, 0, -7]
```

**Output:**
```python
1
```

**Explanation:**

The altitudes are `[0, -5, -4, 1, 1, -6]`.

The maximum altitude is `1`.

### Example 2

**Input:**
```python
gain = [-4, -3, -2, -1, 4, 3, 2]
```

**Output:**
```python
0
```

**Explanation:**

The altitudes are `[0, -4, -7, -9, -10, -6, -3, -1]`.

The maximum altitude is `0`.

---

## My Approach — In-Place Cumulative Sum

I understood that each value in `gain` represents an altitude change, not the actual altitude.

To calculate the actual altitude at every point, I decided to use a running sum.

### Steps

1. Insert `0` at the beginning of the array because the biker starts at altitude `0`.
2. Traverse the array and add each previous altitude to the next gain value.
3. Update the array directly to store the cumulative altitudes.
4. Return the maximum element using `max()`.

This approach calculates all the altitudes without creating a separate list.

---

## My Python Solution

```python
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gain.insert(0, 0)
        for i in range(len(gain)-1):
            gain[i + 1] = gain[i + 1] + gain[i]
        return max(gain)
```

---

## Step-by-Step Dry Run

**Input:**
```python
gain = [-4, -3, -2, -1, 4, 3, 2]
```

### Step 1 — Insert the starting altitude

```python
gain.insert(0, 0)
```

Now:

```python
gain = [0, -4, -3, -2, -1, 4, 3, 2]
```

### Step 2 — Calculate cumulative altitudes

For each iteration:

```python
gain[i + 1] = gain[i + 1] + gain[i]
```

| Iteration | Calculation | Updated altitude |
|---|---|---|
| i = 0 | -4 + 0 | -4 |
| i = 1 | -3 + (-4) | -7 |
| i = 2 | -2 + (-7) | -9 |
| i = 3 | -1 + (-9) | -10 |
| i = 4 | 4 + (-10) | -6 |
| i = 5 | 3 + (-6) | -3 |
| i = 6 | 2 + (-3) | -1 |

After completing the loop:

```python
gain = [0, -4, -7, -9, -10, -6, -3, -1]
```

### Step 3 — Find the maximum altitude

```python
return max(gain)
```

**Output:**
```python
0
```

The highest altitude is `0`, which is the starting altitude.

---

## Edge Case — All Negative Gains

**Input:**
```python
gain = [-3, -2, -4]
```

**After inserting 0:**
```python
[0, -3, -2, -4]
```

**After calculating cumulative altitudes:**
```python
[0, -3, -5, -9]
```

**Output:**
```python
0
```

Even though every altitude change is negative, the highest altitude remains `0` because the biker starts at that altitude.

This is why including the starting altitude is important.

---

## Complexity Analysis

### Time Complexity — O(n)

- Inserting `0` at the beginning of a Python list takes O(n) time because existing elements must be shifted.
- The loop calculates cumulative altitudes in O(n) time.
- `max(gain)` traverses the array in O(n) time.

**Overall: O(n) + O(n) + O(n) = O(n)**

### Auxiliary Space Complexity — O(1)

The algorithm updates the original input list directly and uses no additional list or other data structure proportional to the input size.

Therefore, the auxiliary space complexity is **O(1)**.

**Note:** This solution modifies the input array.

---

## Submission Results

| Metric | Result |
|---|---|
| Status | Accepted |
| Test Cases | 80 / 80 passed |
| Runtime | 0 ms |
| Runtime Beats | 100.00% |
| Memory | 19.20 MB |
| Memory Beats | 64.42% |
| Submission Date | November 28, 2026 |

*Runtime and memory results may vary between submissions.*

---

## Mistake I Made and How I Fixed It

### Initial mistake — Index Out of Range

My original loop was:

```python
for i in range(len(gain)):
    gain[i + 1] = gain[i + 1] + gain[i]
```

**Problem:**

When `i` reaches the last valid index, `i + 1` goes beyond the array boundary.

For example, if the array has 8 elements, the valid indices are `0` through `7`.

When `i = 7`, the expression `gain[i + 1]` tries to access `gain[8]`, causing an `IndexError`.

### My Correction

```python
for i in range(len(gain)-1):
```

This ensures that `i + 1` always remains within the valid index range.

After correcting the loop boundary, my solution passed all 80 test cases.

---

## What I Learned

- How to calculate cumulative sums in an array.
- Why the starting altitude `0` must be considered.
- How to modify an array in place.
- How to use `max()` to find the highest value.
- How to prevent index-out-of-range errors when accessing `i + 1`.
- How to test an algorithm using edge cases such as all-negative values.
- Why understanding loop boundaries is important for correct implementation.

## Key Takeaway

This problem strengthened my understanding of **array traversal, cumulative sums, indexing, and in-place updates**.

I developed the approach independently, encountered an indexing error, corrected it, and successfully submitted the solution.

**Time Complexity:** O(n)  
**Auxiliary Space Complexity:** O(1)

**LeetCode Progress:** Problem 17 / 20 toward my first milestone.
