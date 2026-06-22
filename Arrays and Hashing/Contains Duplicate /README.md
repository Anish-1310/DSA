# Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## My Thought Process

The first idea that came to mind was sorting the array. Once the array is sorted, any duplicate values will appear next to each other, so I can simply compare adjacent elements.

While this works, sorting takes O(n log n) time.

I then looked for a way to avoid sorting altogether. Using a Set allows me to keep track of numbers I've already seen. As I iterate through the array, if a number already exists in the Set, I know a duplicate has been found immediately.

This improves the time complexity to O(n) at the cost of extra space.

---

## Approach

### Solution 1: Sorting

1. Sort the array.
2. Traverse the array from left to right.
3. Compare each element with its previous element.
4. If they are equal, return `True`.
5. If no duplicates are found, return `False`.

### Solution 2: Hash Set

1. Create an empty Set.
2. Traverse the array.
3. Check if the current number already exists in the Set.
4. If it does, return `True`.
5. Otherwise, add the number to the Set.
6. If the traversal finishes, return `False`.

---

## Complexity

### Solution 1: Sorting

**Time Complexity:** O(n log n)

**Space Complexity:** O(1) or O(n) depending on the sorting implementation

### Solution 2: Hash Set

**Time Complexity:** O(n)

**Space Complexity:** O(n)

---

## What I Learned

- Sorting can simplify problems by placing similar values together.
- Sets provide O(1) average lookup time, making them useful for detecting duplicates efficiently.
- Sometimes using additional memory is worthwhile if it significantly improves runtime.
- It's important to compare different approaches and understand the tradeoff between time and space complexity.

---

## Code

See `Solution3_hashset.py`.