"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================
"""

# Linear search: checks items one-by-one from index 0.
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Binary search: splits the search range in half each loop iteration.
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


def test_binary_search_handles_empty_array():
    """Requirement 6 test logic adapted for Python."""
    empty_scores = []
    result = binary_search(empty_scores, 81)
    assert result == -1, f"Expected -1, but got {result}"
    print("test_binary_search_handles_empty_array: PASSED")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ------------------------------
    # Requirement 6: Empty Array Test
    # ------------------------------
    test_binary_search_handles_empty_array()

    # ------------------------------
    # Small dataset test
    # ------------------------------
    print("\n=== SMALL DATASET TEST ===")
    small_data = [4, 12, 23, 35, 47, 56, 68, 79, 88, 91]
    print("Data:", small_data)

    val1 = 47
    print(f"Searching for {val1} (exists):")
    print("Linear:", linear_search(small_data, val1))
    print("Binary:", binary_search(small_data, val1))

    val2 = 50
    print(f"Searching for {val2} (missing):")
    print("Linear:", linear_search(small_data, val2))
    print("Binary:", binary_search(small_data, val2))

    # ------------------------------
    # Large dataset test
    # ------------------------------
    print("\n=== LARGE DATASET TEST ===")
    large_data = list(range(0, 200000, 2))
    target_large = 199998

    print(f"Dataset size: {len(large_data)}")
    print(f"Searching for last element: {target_large}")
    print("Linear search index:", linear_search(large_data, target_large))
    print("Binary search index:", binary_search(large_data, target_large))

    # ------------------------------
    # Edge cases
    # ------------------------------
    print("\n=== EDGE CASE TESTS ===")

    empty = []
    print("Empty list test (looking for 10):")
    print("Linear:", linear_search(empty, 10))
    print("Binary:", binary_search(empty, 10))

    first_val = small_data[0]
    print(f"\nTarget at index 0 ({first_val}):")
    print("Linear:", linear_search(small_data, first_val))
    print("Binary:", binary_search(small_data, first_val))

    one_elem = [42]
    print("\nSingle-item list [42]:")
    print("Binary (found):", binary_search(one_elem, 42))
    print("Binary (not found):", binary_search(one_elem, 99))


if __name__ == "__main__":
    main()

