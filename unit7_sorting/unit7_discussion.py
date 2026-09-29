"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)

- Merge Sort (recursive, divide-and-conquer)


Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
- Create a copy of the original list.

- Compare adjacent elements.

- Swap elements when they are out of order.

- Continue until the list is sorted.

- Return the sorted list.

- Add meaningful comments.


    """
    # make a copy so we don't mutate the original input list
    arr = list(lst)
    n = len(arr)

    # loop through the entire list
    for i in range(n):
        swapped = False
        # inner loop walks up to the unsorted boundary
        for j in range(0, n - i - 1):
            # compare neighboring values
            if arr[j] > arr[j + 1]:
                # swap if the left item is bigger
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # if nothing swapped, the list is already sorted early
        if not swapped:
            break

    return arr


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
- Use recursion.

- Divide the list into smaller halves.

- Sort each half recursively.

- Merge the sorted halves together.

- Return the sorted list.

- Add meaningful comments.


    """
    # base case: lists with 0 or 1 item are already sorted
    if len(lst) <= 1:
        return list(lst)

    # find middle index and split into halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # recursively sort both sides
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # stitch them back together in order
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
- Compare values from the left and right lists.

- Build a new sorted result list.

- Append any remaining values.

- Return the merged sorted list.

- Add meaningful comments.

    """
    result = []
    i = 0
    j = 0

    # pull the smaller value from either left or right until one list empties
    while i < len(left) and j < len(right):
        # using <= preserves stability for identical values
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # tack on any leftovers
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    dataset1 = [42, 17, 88, 5, 23, 91, 12, 64]
    print(f"Original:   {dataset1}")
    print(f"Bubble Sort: {bubble_sort(dataset1)}")
    print(f"Merge Sort:  {merge_sort(dataset1)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    dataset2 = [105, 3, 54, 19, 72, 38, 99, 14, 6]
    print(f"Original:   {dataset2}")
    bubble_res2 = bubble_sort(dataset2)
    merge_res2 = merge_sort(dataset2)
    print(f"Bubble Sort: {bubble_res2}")
    print(f"Merge Sort:  {merge_res2}")
    print(f"Match check: {bubble_res2 == merge_res2}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Case 1: Empty list
    empty_list = []
    print("\n-- Test 1: Empty List --")
    print(f"Input:       {empty_list}")
    print(f"Bubble Sort: {bubble_sort(empty_list)}")
    print(f"Merge Sort:  {merge_sort(empty_list)}")
    print("Explanation: Bubble sort skips the range loops entirely. Merge sort hits len <= 1 base case immediately.")

    # Case 2: Duplicates
    dup_list = [5, 1, 3, 5, 2, 1, 5]
    print("\n-- Test 2: List with Duplicates --")
    print(f"Input:       {dup_list}")
    print(f"Bubble Sort: {bubble_sort(dup_list)}")
    print(f"Merge Sort:  {merge_sort(dup_list)}")
    print("Explanation: Both algorithms handle duplicates cleanly without infinite loops, keeping duplicate values grouped.")

    # Case 3: Reverse sorted
    reverse_list = [9, 7, 5, 3, 1]
    print("\n-- Test 3: Reverse-Sorted List --")
    print(f"Input:       {reverse_list}")
    print(f"Bubble Sort: {bubble_sort(reverse_list)}")
    print(f"Merge Sort:  {merge_sort(reverse_list)}")
    print("Explanation: This is the worst-case scenario for Bubble Sort (max swaps needed). Merge Sort handles it in standard O(n log n).")


if __name__ == "__main__":
    main()