# Majority Element

## Problem

Given an integer array `nums`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

---

## My Thought Process

The first thing I noticed was that the majority element appears more than half the time. Since there's guaranteed to be one, I decided to check the frequency of each unique number.

I iterate through each distinct element using a set, count how many times it appears in the original array, and return the one whose count is greater than or equal to half of the array size.

Although this approach is straightforward and easy to understand, repeatedly counting elements makes it less efficient.

---

## Approach

1. Convert the array into a set to remove duplicate values.
2. Iterate through each unique element.
3. Count its occurrences in the original array.
4. Return the element whose count is at least half the array length.

---

## Complexity

**Time Complexity:** O(n²)

**Space Complexity:** O(n)

---

## What I Learned

- Using a `set` is a simple way to avoid checking duplicate values.
- The `count()` method is convenient but scans the entire array each time, making it inefficient for large inputs.
- There are more optimal solutions (such as the Boyer-Moore Voting Algorithm) that solve this problem in O(n) time and O(1) space.

---

## Code

See `Solution.py`.