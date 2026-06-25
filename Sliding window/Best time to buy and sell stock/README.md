# Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

---

## My Thought Process

My first thought was to compare every buying day with every possible selling day after it. While this would find the correct answer, it requires checking all possible pairs, resulting in O(n²) time.

Instead, I realized that I only need to remember the lowest stock price seen so far. As I move through the array, I calculate the profit if I sold on the current day. If this profit is greater than the maximum profit found so far, I update it.

This allows the problem to be solved in a single pass through the array.

---

## Approach

1. Initialize the minimum price as the first day's price.
2. Initialize the maximum profit as `0`.
3. Traverse the array once.
4. If the current price is lower than the minimum price, update the minimum price.
5. Otherwise, calculate the current profit.
6. Update the maximum profit if the current profit is larger.
7. Return the maximum profit.

---

## Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(1)

---

## What I Learned

- Keeping track of the minimum value seen so far can eliminate the need for nested loops.
- Sometimes storing a small amount of information while traversing an array is enough to optimize a brute-force solution.
- A single-pass algorithm can significantly improve performance from O(n²) to O(n).
- Greedy thinking works well when the optimal decision depends only on previously seen information.

---

## Code

See `Solution.py`.