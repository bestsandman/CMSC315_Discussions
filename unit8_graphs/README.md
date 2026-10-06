# Unit 8 Discussion: Breadth-First Search (BFS)

## Implementation Summary

In this assignment, I implemented Breadth-First Search (BFS) in Python to traverse an unweighted network.

- Data Representation: Modeled a movie recommendation network with 7 nodes using an adjacency list 
(Python dictionary).
- Queue Implementation: Used `collections.deque` to maintain a FIFO queue structure, ensuring nodes were processed 
level by level.
- Cycle Prevention: Used a Python `set` to track visited nodes to avoid infinite loops and duplicate traversals.
- Graph Updates: Added a new node (`Arrival`) and an edge connecting it to `The Martian`, demonstrating how BFS expands 
dynamically to deeper levels.
- Edge Cases Tested: Validated edge cases including an empty graph, non-existent starting nodes, and disconnected 
sub-graphs.

## Discussion Board Reflection

While working on this assignment, I reinforced how graph structures are represented using adjacency lists in Python and 
how a FIFO queue dictates the search pattern in Breadth-First Search (BFS). One challenge I ran into was handling edge 
cases cleanly—specifically avoiding `KeyError` exceptions when an arbitrary starting node was passed or when an isolated 
component was traversed. I resolved this by adding defensive membership checks before initiating the queue loop.

Conceptually, BFS explores graphs radially across concentric layers, making it the ideal choice for finding the shortest 
path on unweighted graphs or discovering closest neighbors (such as finding 1st- and 2nd-degree connections on LinkedIn).
In contrast, Depth-First Search (DFS) dives down a single branch as far as possible before backtracking. DFS is generally
better suited for problems requiring exhaustive exploration, such as maze solving, cycle detection, or evaluating decision
trees. Understanding the difference between a queue-driven BFS and a stack-driven DFS makes it much easier to select the 
right tool depending on whether breadth or depth matters more for the task.