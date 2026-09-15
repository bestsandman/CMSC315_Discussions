"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================
"""

# Linear search: checks items one-by-one from index 0.
# Time complexity is O(n) because worst case (target at end or missing),
# it has to iterate through every single item in the list.
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Binary search: splits the search range in half each loop iteration.
# Assumes the list is sorted. It cuts the remaining elements by 2 each pass,
# which makes the runtime logarithmic O(log n).
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ------------------------------
    # Small dataset test
    # ------------------------------
    print("\n=== SMALL DATASET TEST ===")
    small_data = [4, 12, 23, 35, 47, 56, 68, 79, 88, 91]
    print("Data:", small_data)

    # Test value that exists
    val1 = 47
    print(f"Searching for {val1} (exists):")
    print("Linear:", linear_search(small_data, val1))
    print("Binary:", binary_search(small_data, val1))

    # Test value that does not exist
    val2 = 50
    print(f"Searching for {val2} (missing):")
    print("Linear:", linear_search(small_data, val2))
    print("Binary:", binary_search(small_data, val2))
    # Both find 47 at index 4 and return -1 for 50.
    # At this size (10 items), both finish practically instantly.

    # ------------------------------
    # Large dataset test
    # ------------------------------
    print("\n=== LARGE DATASET TEST ===")
    # List of 100,000 even numbers
    large_data = list(range(0, 200000, 2))
    target_large = 199998  # last element

    print(f"Dataset size: {len(large_data)}")
    print(f"Searching for last element: {target_large}")

    print("Linear search index:", linear_search(large_data, target_large))
    print("Binary search index:", binary_search(large_data, target_large))
    # For linear search, this takes 100,000 comparisons (worst case).
    # Binary search only takes around 17 steps because it cuts the list in half
    # each time (100k -> 50k -> 25k etc.), which is why log n scales so well.

    # ------------------------------
    # Edge cases
    # ------------------------------
    print("\n=== EDGE CASE TESTS ===")

    # Case 1: Empty list
    empty = []
    print("Empty list test (looking for 10):")
    print("Linear:", linear_search(empty, 10))
    print("Binary:", binary_search(empty, 10))
    # Returns -1 immediately. Linear loop doesn't execute;
    # binary search condition (0 <= -1) is false from the start.

    # Case 2: Target is the very first element
    first_val = small_data[0]
    print(f"\nTarget at index 0 ({first_val}):")
    print("Linear:", linear_search(small_data, first_val))
    print("Binary:", binary_search(small_data, first_val))
    # Linear gets this on the first check (best case O(1)),
    # whereas binary still has to halve down to index 0.

    # Case 3: Single-item list
    one_elem = [42]
    print("\nSingle-item list [42]:")
    print("Binary (found):", binary_search(one_elem, 42))
    print("Binary (not found):", binary_search(one_elem, 99))


if __name__ == "__main__":
    main()