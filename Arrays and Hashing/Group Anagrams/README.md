# Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together.

---

## My Thought Process

Since anagrams contain the same characters, sorting them produces the same result.

For example:

- "eat" → "aet"
- "tea" → "aet"
- "ate" → "aet"

So I can use the sorted version of each word as a key in a hash map and group words that share the same key.

---

## Approach

### Hash Map + Sorted Key

- Iterate through each word.
- Sort its characters.
- Use the sorted word as a key.
- Store all matching words in the same group.
- Return all groups.

**Time Complexity:** O(n × k log k)

- `n` = number of strings
- `k` = length of the longest string

**Space Complexity:** O(n × k)

---

## What I Learned

- Converting data into a common form often makes grouping easier.
- Hash maps are perfect for grouping related items.
- Sorting can be used for more than just ordering data.

---

## Code

See `Solution.py`.