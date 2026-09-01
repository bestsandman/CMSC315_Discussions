"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # When inserting an item into a Python list (which is implemented as a dynamic array under the hood),
    # all existing elements at and to the right of the target index must shift one position to the right
    # in contiguous memory to make space for the new value.
    #
    # Performance implications:
    # - Inserting at index 0 (beginning) is O(n) because every single element in the list has to shift right.
    # - Inserting in the middle takes O(n/2) -> O(n) time due to shifting half the elements on average.
    # - Inserting at the end (or appending) takes amortized O(1) time because no elements need to shift.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation is critical in production code to avoid raising an unhandled IndexError,
    # which would crash the application. Checking bounds first ensures graceful degradation.
    # When an element is removed using pop(index), all subsequent elements shift one spot to the left
    # to maintain contiguous memory, resulting in O(n) time complexity unless popping from the very end O(1).
    if 0 <= index < len(lst):
        removed_value = lst.pop(index)
        return removed_value

    # Return None safely if the index is out of bounds or negative
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search: because the list is unsorted and elements are not indexed by key,
    # the algorithm must inspect each element one-by-one from left to right (index 0 to n-1).
    #
    # Performance:
    # - Best case: O(1) if the target value is at the very first index.
    # - Worst / Average case: O(n) if the item is at the end or not present at all.
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Target found, return the matching index

    return -1  # Full sequential scan completed without finding the value


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Step 1: Initialize sample list
    numbers = [20, 30, 40]
    print(f"Original list: {numbers}")

    # Step 2: Insert at the beginning (index 0) - forces all existing items to shift right
    insert_at(numbers, 0, 10)
    print(f"After inserting 10 at beginning (index 0): {numbers}")

    # Step 3: Insert in the middle (index 2) - elements from index 2 onward shift right
    insert_at(numbers, 2, 25)
    print(f"After inserting 25 in middle (index 2): {numbers}")

    # Step 4: Insert at the end (index equal to length) - no elements need to shift
    insert_at(numbers, len(numbers), 50)
    print(f"After inserting 50 at end (index {len(numbers) - 1}): {numbers}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Step 1: Remove from beginning (index 0) - shifts remaining elements left
    removed_first = delete_at(numbers, 0)
    print(f"Removed '{removed_first}' from beginning -> Updated list: {numbers}")

    # Step 2: Remove from middle (index 1) - shifts elements after index 1 left
    removed_mid = delete_at(numbers, 1)
    print(f"Removed '{removed_mid}' from middle (index 1) -> Updated list: {numbers}")

    # Step 3: Remove from end (last index) - no elements shift
    removed_last = delete_at(numbers, len(numbers) - 1)
    print(f"Removed '{removed_last}' from end -> Updated list: {numbers}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Step 1: Search for a target value that exists in the list
    target_found = 40
    idx_found = search_value(numbers, target_found)
    print(f"Searching for {target_found}: Found at index {idx_found}")

    # Step 2: Search for a target value that is absent
    target_missing = 99
    idx_missing = search_value(numbers, target_missing)
    print(f"Searching for {target_missing}: Not found (Returned {idx_missing})")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Attempting to delete using an out-of-bounds index on a non-empty list
    invalid_index = 10
    result_invalid_delete = delete_at(numbers, invalid_index)
    print(f"Edge Case 1 - Deleting invalid index {invalid_index}: Returned {result_invalid_delete} (Handled safely without error)")

    # Edge Case 2: Deleting from an empty list
    empty_list = []
    result_empty_delete = delete_at(empty_list, 0)
    print(f"Edge Case 2 - Deleting from empty list []: Returned {result_empty_delete}")

    # Edge Case 3: Inserting into an empty list
    insert_at(empty_list, 0, "First Item")
    print(f"Edge Case 3 - Inserting into empty list: {empty_list}")


if __name__ == "__main__":
    main()