"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and set children to None initially
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Start with an empty tree where root points to nothing
        self.root = None

    def insert(self, value):
        """
        Public insert method.
        Delegates the work to our recursive helper. We check smaller/larger
        comparisons at each step because preserving this invariant (left < parent < right)
        is what guarantees we can do logarithmic searches later on.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Base case: empty spot found, attach the new node here
        if node is None:
            return Node(value)

        # If incoming value is smaller, branch down the left side
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # If larger, branch down the right side
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # If value is equal, ignore duplicate to keep keys unique
            pass

        return node

    def search(self, value):
        """
        Public search method.
        Instead of checking every single item one-by-one like a linear scan (O(n)),
        a BST search cuts out half the remaining tree at each node comparison.
        This drops average search time down to O(log n).
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        # Base cases: hit an empty branch (not found) or matched the value (found)
        if node is None:
            return False
        if node.value == value:
            return True

        # Narrow our search window depending on the comparison
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """Returns a list containing all tree values in-order."""
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        In-order traversal visits: Left subtree -> Current node -> Right subtree.
        Because a BST forces all smaller values into the left subtree and all
        larger values into the right subtree, visiting 'Left, Current, Right'
        guarantees items are processed in strict ascending order.
        """
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # 1. BUILD A TREE
    # Picking 50 as root so we get a well-balanced distribution
    # on both the left and right subtrees.
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    print("\n=== TREE CONSTRUCTION ===")
    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        tree.insert(val)
    print("Tree constructed successfully.")

    # 2. IN-ORDER TRAVERSAL
    # Running in-order traversal prints out the sorted sequence [20, 30, 40, 50, 60, 70, 80].
    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_values = tree.inorder()
    print(f"In-order traversal output: {sorted_values}")

    # 3. SEARCH TESTS
    print("\n=== SEARCH TESTS ===")
    # Items that exist (one in left subtree, one in right subtree)
    found_targets = [30, 80]
    for target in found_targets:
        result = tree.search(target)
        print(f"Searching for {target}: {'Found' if result else 'Not Found'}")

    # Items that do not exist
    missing_targets = [15, 99]
    for target in missing_targets:
        result = tree.search(target)
        print(f"Searching for {target}: {'Found' if result else 'Not Found'}")

    # 4. EDGE CASES
    print("\n=== EDGE CASES ===")
    # Edge Case 1: Operating on an empty tree
    empty_tree = BST()
    print(f"Traversing empty tree: {empty_tree.inorder()} (safely returns empty list)")
    print(f"Searching empty tree for 50: {empty_tree.search(50)} (safely returns False)")

    # Edge Case 2: Inserting duplicates
    print(f"Attempting to re-insert duplicate 50 into main tree...")
    tree.insert(50)
    print(f"In-order output after duplicate insert: {tree.inorder()} (duplicate cleanly ignored)")


if __name__ == "__main__":
    main()