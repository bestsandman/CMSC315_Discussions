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
    # When inserting into a list, Python has to shift all items at and after
    # the target index one spot to the right to make room.
    #
    # Performance:
    # - Inserting at index 0 is O(n) because every item has to shift.
    # - Inserting in the middle is roughly O(n/2), which is still O(n).
    # - Inserting at the end is O(1) since nothing needs to shift.
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
    # Check if the index is valid first so the program doesn't crash with an IndexError.
    # Using pop() will shift remaining elements left, which takes O(n) time unless popping the last item.
    if 0 <= index < len(lst):
        removed_value = lst.pop(index)
        return removed_value

    # If the index is out of range, return None safely
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
    # This is a basic linear search that checks elements one by one from start to finish.
    # - Best case: O(1) if the element is at the very beginning.
    # - Worst case: O(n) if the element is at the end or not in the list at all.
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Found it, return the index

    return -1  # Reached the end without finding it


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

    # Step 1: Start with a base list
    numbers = [20, 30, 40]
    print(f"Original list: {numbers}")

    # Step 2: Insert at the start (index 0) -> shifts everything right
    insert_at(numbers, 0, 10)
    print(f"After inserting 10 at beginning (index 0): {numbers}")

    # Step 3: Insert in the middle (index 2)
    insert_at(numbers, 2, 25)
    print(f"After inserting 25 in middle (index 2): {numbers}")

    # Step 4: Insert at the end
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

    # Step 1: Remove from the start -> shifts remaining items left
    removed_first = delete_at(numbers, 0)
    print(f"Removed '{removed_first}' from beginning -> Updated list: {numbers}")

    # Step 2: Remove from the middle
    removed_mid = delete_at(numbers, 1)
    print(f"Removed '{removed_mid}' from middle (index 1) -> Updated list: {numbers}")

    # Step 3: Remove from the end -> no shifting needed
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

    # Step 1: Search for an item that is in the list
    target_found = 40
    idx_found = search_value(numbers, target_found)
    print(f"Searching for {target_found}: Found at index {idx_found}")

    # Step 2: Search for an item that isn't in the list
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

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Trying to delete an out-of-bounds index
    invalid_index = 10
    result_invalid_delete = delete_at(numbers, invalid_index)
    print(f"Edge Case 1 - Deleting invalid index {invalid_index}: Returned {result_invalid_delete} (Handled safely)")

    # Edge Case 2: Trying to delete from an empty list
    empty_list = []
    result_empty_delete = delete_at(empty_list, 0)
    print(f"Edge Case 2 - Deleting from empty list []: Returned {result_empty_delete}")

    # Edge Case 3: Inserting into an empty list
    insert_at(empty_list, 0, "First Item")
    print(f"Edge Case 3 - Inserting into empty list: {empty_list}")


if __name__ == "__main__":
    main()