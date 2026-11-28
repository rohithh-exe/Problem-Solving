# 217. Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Hash Set  
**Language:** Python  
**Status:** Accepted (80/80 test cases)

**Problem Link:** https://leetcode.com/problems/contains-duplicate/

---

## Problem Description

Given an integer array `nums`, return `True` if any value appears at least twice in the array. Otherwise, return `False` if every element is distinct.

### Example 1

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Output:**
```python
True
```

**Explanation:** The number `1` appears twice.

### Example 2

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
False
```

**Explanation:** Every element is unique.

---

## My Approach — Using a Set

I already knew that Python sets store only unique elements.

Instead of comparing every pair of elements using nested loops, I realized that I could convert the array into a set and compare their lengths.

**My logic:**

1. Convert the input array into a set using `set(nums)`.
2. The set automatically removes duplicate values.
3. Compare the length of the original array with the length of the set.
4. If the lengths are different, duplicates were present, so return `True`.
5. Otherwise, return `False`.

I independently came up with the length-comparison approach and referred to Python documentation to check set functionality and return-statement syntax.

## My Python Solution

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        checker = set(nums)
        return bool(len(nums) != len(checker))
```

## Step-by-Step Dry Run

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Step 1 — Convert to a set**

```python
checker = set(nums)
```

The set contains:

```python
{1, 2, 3}
```

**Step 2 — Compare lengths**

```python
len(nums)     # 4
len(checker)  # 3
```

**Step 3 — Evaluate the condition**

```python
4 != 3  # True
```

**Final output:**
```python
True
```

Since the set has fewer elements than the original array, at least one duplicate exists.

### Another Example — No Duplicates

**Input:** `[1, 2, 3, 4]`

- Original array length = 4
- Set length = 4
- Comparison: `4 != 4` → `False`

**Output:** `False`

---

## Complexity Analysis

### Time Complexity — O(n) Average

- Creating a set from `n` elements takes O(n) time on average.
- Checking the lengths takes O(1) time.
- Therefore, the overall average time complexity is **O(n)**.

### Space Complexity — O(n)

- The set stores up to `n` unique elements.
- Therefore, the auxiliary space complexity is **O(n)**.

---

## Submission Results

| Metric | Result |
|---|---|
| Status | Accepted |
| Test Cases | 80/80 passed |
| Runtime | 11 ms |
| Runtime Beats | 90.72% |
| Memory | 32.91 MB |
| Memory Beats | 42.69% |

*Results are from my LeetCode submission on November 28, 2026. Runtime and memory percentiles may vary between submissions.*

---

## What I Learned

- How Python sets automatically eliminate duplicate elements.
- How to use a data structure's properties to simplify a problem.
- How to compare collection lengths to detect duplicates.
- How to return a Boolean expression directly from a function.
- How to use Python documentation as a reference without copying a problem's solution.

### Small Improvement

My original implementation uses:

```python
return bool(len(nums) != len(checker))
```

The `bool()` conversion is optional because the `!=` comparison already produces a Boolean.

A simpler equivalent expression is:

```python
return len(nums) != len(checker)
```

Both are correct.

## Key Takeaway

This problem helped me understand that choosing the right data structure can simplify an algorithm significantly.

By using a set and comparing lengths, I solved the problem in **O(n) average time** without needing nested loops.

I developed the approach independently and used external references only to check Python functionality and syntax.
