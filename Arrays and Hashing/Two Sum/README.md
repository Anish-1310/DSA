# Two Sum

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the two numbers whose sum equals the target.

---

## My Thought Process

The first idea that came to mind was checking every pair of numbers. While this works, it requires two nested loops, making it inefficient for large inputs.

To improve this, I used a HashMap to store the numbers I've already seen. For every number, I calculate its complement (`target - current_number`) and check if that complement already exists in the HashMap. If it does, I've found the answer immediately.

---

## Approach

1. Create an empty HashMap.
2. Traverse the array.
3. Calculate the complement.
4. If the complement exists in the HashMap, return the indices.
5. Otherwise, store the current number and continue.

---

## Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(n)

---

## What I Learned

- HashMaps are extremely useful when fast lookups are needed.
- Instead of searching for the second number, it's often easier to search for its complement.
- Sometimes using extra memory is worth it if it significantly reduces the runtime.

---

## Code

See `Two Sum.py`.