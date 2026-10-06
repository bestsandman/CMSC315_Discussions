"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # Quick sanity check: if the graph is empty or the start node isn't in it, return empty
    if not graph or start not in graph:
        return []

    # A queue (FIFO - first in, first out) lets us visit nodes layer by layer.
    # We explore all immediate neighbors first before going deeper.
    queue = deque([start])

    # Keeping track of visited nodes stops us from getting stuck in infinite loops/cycles
    visited = set([start])
    traversal_order = []

    while queue:
        # Pull the next node from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Look through all connected neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # We append neighbors to the back of the queue so they wait their turn
                # until everyone on the current level is processed.
                # Unlike DFS (which uses a stack/recursion to rush straight down a single path),
                # BFS fans out evenly across neighbors.
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # Real-world scenario: Streaming service recommendation network
    # Nodes represent movies/shows, edges represent direct genre/audience similarities
    movie_graph = {
        "Inception": ["Interstellar", "The Matrix", "Memento"],
        "Interstellar": ["Inception", "The Martian"],
        "The Matrix": ["Inception", "Blade Runner"],
        "Memento": ["Inception", "Shutter Island"],
        "The Martian": ["Interstellar"],
        "Blade Runner": ["The Matrix"],
        "Shutter Island": ["Memento"]
    }

    # Print the graph adjacency list
    for movie, recommendations in movie_graph.items():
        print(f"{movie} -> {', '.join(recommendations)}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    start_movie = "Inception"
    print(f"Starting BFS from '{start_movie}'...")

    # Level 0: Inception
    # Level 1: Interstellar, The Matrix, Memento (direct neighbors)
    # Level 2: The Martian, Blade Runner, Shutter Island (neighbors of neighbors)
    order = bfs(movie_graph, start_movie)
    print("Traversal Order (Level by Level):")
    print(" -> ".join(order))

    # Adding a new movie node and connecting it to The Martian
    print("\nAdding 'Arrival' connected to 'The Martian' and re-running BFS...")
    movie_graph["Arrival"] = ["The Martian"]
    movie_graph["The Martian"].append("Arrival")

    updated_order = bfs(movie_graph, start_movie)
    print("Updated Traversal Order:")
    print(" -> ".join(updated_order))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Start node doesn't exist in graph
    missing_movie = "Avatar"
    print(f"\n1. Testing missing start node ('{missing_movie}'):")
    result_missing = bfs(movie_graph, missing_movie)
    print(f"Result: {result_missing} (gracefully handles unknown keys without crashing)")

    # Edge Case 2: Disconnected graph / isolated component
    print("\n2. Testing disconnected graph:")
    disconnected_graph = {
        "Movie A": ["Movie B"],
        "Movie B": ["Movie A"],
        "Movie C": ["Movie D"],  # Isolated sub-network
        "Movie D": ["Movie C"]
    }
    result_disconnected = bfs(disconnected_graph, "Movie A")
    print(f"Starting at 'Movie A': {result_disconnected}")
    print("Explanation: BFS only visits reachable nodes within the connected component.")

    # Edge Case 3: Empty graph
    print("\n3. Testing empty graph:")
    empty_result = bfs({}, "Inception")
    print(f"Result on empty dictionary: {empty_result}")


if __name__ == "__main__":
    main()