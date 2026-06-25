# Remove Duplicates from Sorted Array

## Problem

Given a sorted integer array `nums`, remove the duplicates in-place such that each unique element appears only once.

The relative order of the elements should be kept the same. Return the number of unique elements.

---

## My Thought Process

My first thought was to use a Set since it automatically removes duplicates. However, that would require extra space and wouldn't satisfy the in-place requirement.

Since the array is already sorted, all duplicate values appear next to each other. This means I only need to compare the current element with the last unique element I've kept.

Using two pointers makes this straightforward. One pointer keeps track of the last unique element, while the other scans through the array. Whenever a new unique value is found, it is placed in the next available position.

This allows the array to be updated in-place with only one pass.

---

## Approach

1. Initialize a pointer `l` at the first element.
2. Traverse the array using another pointer `r`.
3. Compare `nums[r]` with `nums[l]`.
4. If they are different, increment `l` and copy `nums[r]` to `nums[l]`.
5. Continue until the traversal is complete.
6. Return `l + 1`, which represents the number of unique elements.

---

## Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

## What I Learned

- A sorted array makes duplicate detection much easier because identical values are adjacent.
- Two pointers are an efficient way to modify arrays in-place.
- Comparing against the last unique element avoids unnecessary operations.
- Leveraging properties of the input (such as sorting) often leads to simpler and more efficient solutions.

---

## Code

See `Solution.py`.