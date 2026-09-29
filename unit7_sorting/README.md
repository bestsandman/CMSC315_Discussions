# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared the design, implementation, and performance characteristics of Bubble Sort and Merge Sort.

## Implementation Summary

- Bubble Sort (`bubble_sort`): Implemented an iterative comparison sort. Created a shallow copy of the input list to 
prevent modifying the original dataset. Added a boolean `swapped` flag to enable early termination if a pass completed
without any swaps (best-case O(n) performance).

- Merge Sort (`merge_sort`): Implemented a recursive divide-and-conquer strategy. Sliced lists down the middle until 
reaching single-element or empty base cases (len <= 1), then sorted the sub-lists recursively.

- Merge Helper (`merge`): Reconstructed sorted lists by comparing values from left and right halves. Maintained 
stability by prioritizing the left element during ties (`<=`), and appended remaining elements using `.extend()`.

- Testing & Edge Cases: Verified algorithm accuracy against two unsorted datasets containing distinct elements. 
Validated robustness against three edge cases: empty lists, datasets containing duplicates, and reverse-sorted lists.

## Learning Objectives Addressed

- Implemented iterative Bubble Sort with early-exit optimization.
- Implemented recursive Merge Sort with a separate merge routine.
- Explored divide-and-conquer logic and recursive call stacks.
- Evaluated runtime trade-offs (O(n^2) vs. O(n log n)) across varying input distributions.

## Discussion Board Reflection
### 1. Concepts and Skills Learned
Building these from scratch made the difference between recursive divide-and-conquer and basic nested loops click for 
me. Actually tracing the call stack and watching how sub-lists break apart and merge back together in order was a lot 
more useful than just reading about it. I also made sure to copy the lists first so the original inputs wouldn't get 
modified.

### 2. Challenges Encountered & Resolutions
My biggest hurdle was in the `merge()` function. I kept running into an `IndexError` when the left and right lists 
weren't the exact same size. Once the main `while` loop finished comparing items, I realized I was dropping remaining 
elements, so using `.extend()` on both slices sorted that out cleanly.

### 3. Algorithm Comparison (Bubble Sort vs. Merge Sort)
Bubble Sort was simple to write and barely takes any extra memory, but the $O(n^2)$ runtime falls apart fast on bigger 
datasets—especially on the reverse-sorted test. Merge Sort takes extra memory to store the sliced sub-arrays, but the
consistent O(n log n) speed makes it the clear choice if you're dealing with larger, real-world data.