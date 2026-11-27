# LeetCode 1773 — Count Items Matching a Rule

**Difficulty:** Easy  
**Topics:** Arrays, Strings, Conditional Statements  
**Language:** Python  
**Status:** Solved

## Problem Statement

You are given a list `items`, where each item contains three strings in the following order:

`[type, color, name]`

You are also given two strings:

- `ruleKey`: One of `"type"`, `"color"`, or `"name"`.
- `ruleValue`: The value that must be matched.

Return the number of items that match the given rule.

### Example 1

**Input:**
```python
items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]
ruleKey = "color"
ruleValue = "silver"
```

**Output:**
```python
1
```

**Explanation:** Only the second item has the color `"silver"`.

### Example 2

**Input:**
```python
items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "phone"],
    ["phone", "gold", "iphone"]
]
ruleKey = "type"
ruleValue = "phone"
```

**Output:**
```python
2
```

**Explanation:** The first and third items have the type `"phone"`.

## My Approach — Linear Traversal with Conditional Statements

I solved this problem using a `for` loop and an `if-elif` conditional structure.

Each item contains three values:
- Index `0` represents the type.
- Index `1` represents the color.
- Index `2` represents the name.

I check which property is requested by `ruleKey` and compare its corresponding value with `ruleValue`.

Whenever both conditions match, I increment the counter.

### Algorithm

1. Initialize `count = 0`.
2. Traverse every item in `items`.
3. If `ruleKey` is `"type"`, compare `i[0]` with `ruleValue`.
4. Otherwise, if `ruleKey` is `"color"`, compare `i[1]` with `ruleValue`.
5. Otherwise, if `ruleKey` is `"name"`, compare `i[2]` with `ruleValue`.
6. Increment `count` whenever a matching item is found.
7. Return the final count.

## Python Solution

```python
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == "type" and i[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and i[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and i[2] == ruleValue:
                count += 1
        return count
```

## Step-by-Step Dry Run

**Input:**

```python
items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]
ruleKey = "color"
ruleValue = "silver"
```

| Iteration | Current Item | Color | Matches? | Count |
|---|---|---|---|---|
| 1 | phone, blue, pixel | blue | No | 0 |
| 2 | computer, silver, lenovo | silver | Yes | 1 |
| 3 | phone, gold, iphone | gold | No | 1 |

**Final Output:**

```python
1
```

## Complexity Analysis

### Time Complexity: O(n)

The `for` loop traverses all `n` items exactly once.

Each item requires at most three conditional checks. Since the number of checks is constant:

**Time Complexity = O(n)**

### Auxiliary Space Complexity: O(1)

The program uses only a counter and a loop variable.

It does not create any additional array or data structure proportional to the input size.

**Auxiliary Space Complexity = O(1)**

## Submission Performance

| Metric | Result |
|---|---|
| Runtime | 4 ms |
| Runtime Beats | 5.90% |
| Memory | 23.62 MB |
| Memory Beats | 27.56% |

These measurements may vary between submissions.

The solution already has optimal asymptotic time complexity because each item may need to be examined.

## What I Learned

- How to traverse nested lists in Python.
- How to access individual properties using list indices.
- How to combine conditions using the `and` operator.
- How to use `if-elif` statements to handle multiple cases.
- How to count matching elements using a counter.
- How to distinguish between iterating over values and indices.
- How to analyze O(n) time and O(1) auxiliary space complexity.

## Conclusion

I independently solved LeetCode #1773 using a linear traversal and conditional statements.

This problem strengthened my understanding of nested lists, indexing, logical conditions, and converting a problem statement into a working Python implementation.

**Time Complexity:** O(n)  
**Auxiliary Space Complexity:** O(1)